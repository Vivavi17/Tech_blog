from fastapi import Depends, Request
from src.exceptions import TokenAbsentException
from jose import jwt
from src.config import settings
from src.exceptions import IncorrectTokenFormatException, UserDoesntExistsException, UserRightsException
from src.users.dao import UsersDAO


async def get_token(request: Request) -> str:
    token = request.cookies.get("tech_blog")
    if not token:
        raise TokenAbsentException
    return token

async def check(access_token:str, status=None):
    payload = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
    if not (user_id := payload.get("sub")):
        raise IncorrectTokenFormatException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserDoesntExistsException
    if user.ban:
        raise UserRightsException
    if status and status != user.status:
        raise UserDoesntExistsException
    return user

async def check_admin(access_token: str = Depends(get_token)):
    return await check(access_token, "Admin")


async def check_user(access_token: str = Depends(get_token)):
    return await check(access_token)

