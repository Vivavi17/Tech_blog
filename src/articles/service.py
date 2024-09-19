"""Бизнес-логика работы со статьями"""

from typing import Optional

from src.articles.dao import ArticlesDAO
from src.articles.models import Articles
from src.base.singleton import Singleton
from src.exceptions import ArticleNotFoundException, UserRightsException
from src.users.models import Users


class ArticlesService(Singleton):
    """Класс с логикой работы со статьями"""

    dao = ArticlesDAO

    async def add_new_article(self, user_id: int, article_type: str, description: str):
        """Добавить новую статью"""
        return await self.dao.add(
            author_id=user_id, type=article_type, description=description
        )

    async def get_article(self, article_id: int) -> Articles:
        """Получить новую статью по артиклю"""
        return await self.find_article(id=article_id)

    async def find_article(self, **kwargs):
        """Получить новую статью фильтру"""
        article = await self.dao.find_one_or_none(**kwargs)
        if not article:
            raise ArticleNotFoundException
        return article

    async def get_articles(
        self,
        articles_type: Optional[str],
        author_id: Optional[int],
        limit: int,
        offset: int,
        order_by: str,
    ):
        """Получить список статей по фильтру с сортировкой и пагинацией"""
        filter_by = {
            k: v
            for k, v in [["type", articles_type], ["author_id", author_id]]
            if v is not None
        }
        return await self.dao.find_all(limit, offset, order_by, **filter_by)

    async def del_article(self, article_id: int, user_id: int):
        """Удалить статью по id (доступно только автору статьи)"""
        article = await self.find_article(id=article_id)
        if article.author_id != user_id:
            raise UserRightsException
        await self.dao.delete(id=article_id)

    async def set_type(self, article_id: int, article_type: str, user: Users):
        """Изменить тип статьи (доступно автору и АДМ)"""
        article = await self.find_article(id=article_id)
        if not (article.author_id == user.id or user.status == "Admin"):
            raise UserRightsException
        edited_article = await self.dao.update(article.id, type=article_type)
        return edited_article


articles_service = ArticlesService()
