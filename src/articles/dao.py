from src.common.base_dao import BaseDAO
from src.articles.models import Articles
from src.database import async_session_maker
from sqlalchemy import select


class ArticlesDAO(BaseDAO):
    model = Articles

    @classmethod
    async def find_all(cls, limit, offset, order_by, **filter_by):
        """Получение последних версий тендеров с фильтрацией и пагинацией"""
        filter_by = {k: v for k, v in filter_by.items() if v is not None}
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
