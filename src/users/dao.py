"""Модуль с работой запросов к таблице пользователей"""

from sqlalchemy import func, select

from src.base.base_dao import BaseDAO
from src.database import async_session_maker
from src.users.models import Users


class UsersDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс с логикой запросов к таблице пользователей"""

    model = Users

    @classmethod
    async def count(cls):
        """Количество  записей"""
        async with async_session_maker() as session:
            query = select(func.count("*")).select_from(  # pylint: disable=not-callable
                cls.model
            )
            result = await session.execute(query)
            return result.scalar_one()
