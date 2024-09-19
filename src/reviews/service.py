"""Бизнес-логика работы отзывов"""

from src.articles.service import articles_service
from src.base.singleton import Singleton
from src.reviews.dao import ReviewsDAO


class ReviewsService(Singleton):  # pylint: disable=too-few-public-methods
    """Логика работы с отзывами"""

    dao = ReviewsDAO

    async def add_review(self, author_id: int, article_id: int, description: str):
        """Добавить отзыв на статью"""
        await articles_service.find_article(id=article_id)
        return await self.dao.add(
            author_id=author_id, article_id=article_id, description=description
        )


reviews_service = ReviewsService()
