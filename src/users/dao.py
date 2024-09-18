"""Модуль с работой запросов к таблице пользователей"""

from sqlalchemy import select, func

from src.common.base_dao import BaseDAO
from src.users.models import Users
from src.database import async_session_maker


class UsersDAO(BaseDAO):
    """Класс с логикой запросов к таблице пользователей"""

    model = Users
    @classmethod
    async def count(cls):
        """Количество  записей"""
        async with async_session_maker() as session:
            query = select(func.count("*")).select_from(cls.model)
            result = await session.execute(query)
            return result.scalar_one()
