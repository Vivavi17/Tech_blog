"""Модуль релизации зависимостей"""

from fastapi import Depends, Request
from jose import ExpiredSignatureError, jwt

from src.config import settings
from src.exceptions import (IncorrectTokenFormatException,
                            TokenAbsentException, TokenExpiredException,
                            UserBannnedException, UserDoesntExistsException,
                            UserRightsException)
from src.users.dao import UsersDAO


async def get_token(request: Request) -> str:
    """Получить токен"""
    token = request.cookies.get("tech_blog")
    if not token:
        raise TokenAbsentException
    return token


async def check(access_token: str, status=None):
    """Проверка токена пользователей"""
    try:
        payload = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError as exp_error:
        raise TokenExpiredException from exp_error
    if not (user_id := payload.get("sub")):
        raise IncorrectTokenFormatException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserDoesntExistsException
    if user.ban:
        raise UserBannnedException
    if status and status != user.status:
        raise UserRightsException
    return user


async def check_admin(access_token: str = Depends(get_token)):
    """Проверка админа"""
    return await check(access_token, "Admin")


async def check_user(access_token: str = Depends(get_token)):
    """Проверка пользователя"""
    return await check(access_token)
