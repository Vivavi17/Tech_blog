"""Модуль с бизнес-логикой жалоб"""

from typing import Optional

from src.articles.service import articles_service
from src.base.singleton import Singleton
from src.complaints.dao import ComplaintsDAO


class ComplaintsService(Singleton):
    """Класс работы с жалобами"""

    dao = ComplaintsDAO

    async def get_complaints(
        self,
        article_id: Optional[int],
        author_id: Optional[int],
        limit: int,
        offset: int,
        order_by: str,
    ):
        """Получить список жалоб"""
        filter_by = {
            k: v
            for k, v in [["article_id", article_id], ["author_id", author_id]]
            if v is not None
        }
        return await self.dao.find_all(limit, offset, order_by, **filter_by)

    async def add_new_complaint(self, user_id: int, article_id: int, description: str):
        """Добавить жалобу"""
        await articles_service.find_article(id=article_id)
        return await self.dao.add(
            author_id=user_id, article_id=article_id, description=description
        )


complaints_service = ComplaintsService()
