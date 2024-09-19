"""Бизнес-логика работы пользователей"""

from fastapi import Response
from pydantic import EmailStr

from src.base.singleton import Singleton
from src.exceptions import (IncorrectLoginOrPasswordException,
                            UserAlreadyExistsException, UserBannnedException,
                            UserDoesntExistsException)
from src.users.auth import create_access_token, get_hashed_pwd, verify_pwd
from src.users.dao import UsersDAO


class UsersService(Singleton):
    """Логика работы пользователей"""

    dao = UsersDAO

    async def find_user(self, **kwargs):
        """Найти пользователя по фильтру"""
        user = await self.dao.find_one_or_none(**kwargs)
        if not user:
            raise UserDoesntExistsException
        return user

    async def register(self, username: str, email: EmailStr, password: str) -> None:
        """Добавить запись пользователя"""
        is_exist = await self.dao.find_one_or_none(email=email)
        if is_exist:
            raise UserAlreadyExistsException
        users = await self.dao.count()
        status = "User"
        if not users:
            status = "Admin"
        hashed_password = get_hashed_pwd(password)
        await self.dao.add(
            username=username,
            email=email,
            hashed_password=hashed_password,
            status=status,
        )

    async def login(self, response: Response, email: EmailStr, password: str) -> str:
        """Входу в учетную запись"""
        user = await self.find_user(email=email)
        if not verify_pwd(password, user.hashed_password):
            raise IncorrectLoginOrPasswordException
        if user.ban:
            raise UserBannnedException
        access_token = create_access_token({"sub": str(user.id), "status": user.status})
        response.set_cookie("tech_blog", access_token, httponly=True)
        return access_token

    async def set_status(self, user_id: int, status):
        """Изменить статус пользователя"""
        await self.find_user(id=user_id)
        await self.dao.update(user_id, status=status)

    async def set_ban(self, user_id: int, ban: bool):
        """Забанить/разбанить пользователя"""
        await self.find_user(id=user_id)
        await self.dao.update(user_id, ban=ban)

    async def logout(self, response: Response):
        """Выйти из учетной записи"""
        response.delete_cookie("tech_blog")


users_service = UsersService()
