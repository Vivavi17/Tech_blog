"""Бизнес-логика работы комментариев"""

from src.articles.service import articles_service
from src.comments.dao import CommentsDAO
from src.common.singleton import Singleton


class CommentsService(Singleton):
    """Класс с логикой работы комментариев"""

    dao = CommentsDAO

    async def add_new_comment(self, user_id: int, article_id: int, description: str):
        """Добавить новый комментарий"""
        await articles_service.find_article(id=article_id)
        return await self.dao.add(
            author_id=user_id, article_id=article_id, description=description
        )

    async def del_comment(self, comment_id: int) -> None:
        """Удалить комментарий по id"""
        await self.dao.delete(id=comment_id)


comments_service = CommentsService()
