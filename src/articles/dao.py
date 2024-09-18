"""модуль для работы с таблицей статей"""

from sqlalchemy import select

from src.articles.models import Articles
from src.common.base_dao import BaseDAO
from src.database import async_session_maker


class ArticlesDAO(BaseDAO):
    """Класс с запросами в таблицу статей"""

    model = Articles

    @classmethod
    async def find_all(cls, limit, offset, order_by, **filter_by):
        """Получение статей с фильтрацией и пагинацией"""
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
