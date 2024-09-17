from fastapi import Depends, Request, Response
from pydantic import EmailStr

from src.exceptions import (IncorrectLoginOrPasswordException,
                            UserAlreadyExistsException,
                            UserDoesntExistsException)
from src.users.auth import create_access_token, get_hashed_pwd, verify_pwd
from src.users.dao import UsersDAO
from src.users.models import Users


class UsersService:
    singleton = None
    dao = UsersDAO

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton

    async def register(self, username: str, email: EmailStr, password: str):
        is_exist = await self.dao.find_one_or_none(email=email)
        if is_exist:
            raise UserAlreadyExistsException
        hashed_password = get_hashed_pwd(password)
        await self.dao.add(
            username=username, email=email, hashed_password=hashed_password
        )

    async def login(self, response: Response, email: EmailStr, password: str) -> str:
        user = await self.dao.find_one_or_none(email=email)
        if not user or not verify_pwd(password, user.hashed_password) or user.ban:
            raise IncorrectLoginOrPasswordException
        access_token = create_access_token({"sub": str(user.id), "status": user.status})
        response.set_cookie("tech_blog", access_token, httponly=True)
        return access_token

    async def set_status(self, user_id: int, status):
        user = await self.dao.find_one_or_none(id=user_id)
        if not user:
            raise UserDoesntExistsException
        await self.dao.update(user_id, status=status)

    async def set_ban(self, user_id: int, ban: bool):
        user = await self.dao.find_one_or_none(id=user_id)
        if not user:
            raise UserDoesntExistsException
        await self.dao.update(user_id, ban=ban)

    async def logout(self, response: Response):
        response.delete_cookie("tech_blog")


users_service = UsersService()
