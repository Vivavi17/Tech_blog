"""Модуль с запросами к таблице жалоб"""

from sqlalchemy import select

from src.common.base_dao import BaseDAO
from src.complaints.models import Complaints
from src.database import async_session_maker


class ComplaintsDAO(BaseDAO):
    """Класс для работы с таблицей жалоб"""

    model = Complaints

    @classmethod
    async def find_all(cls, limit, offset, order_by, **filter_by):
        """Получение жалоб с фильтрацией, сортировкой и пагинацией"""
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__)
                .filter_by(**filter_by)
                .order_by(order_by)
                .offset(offset)
                .limit(limit)
            )
            result = await session.execute(query)
        return result.mappings().all()
