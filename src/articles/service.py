from typing import Optional

from src.articles.dao import ArticlesDAO
from src.articles.models import Articles
from src.exceptions import ArticleNotFoundException, UserRightsException
from src.users.models import Users


class ArticlesService:
    singleton = None
    dao = ArticlesDAO

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton

    async def add_new_article(self, user_id: str, type: str, description: str):
        return await self.dao.add(author_id=user_id, type=type, description=description)

    async def get_article(self, article_id: int) -> Articles:
        return await self.dao.find_one_or_none(id=article_id)

    async def get_articles(self, articles_type: Optional[str], author_id: Optional[str], limit: int, offset: int,
                           order_by: str):
        filter_by = {k: v for k, v in [["type", articles_type], ["author_id", author_id]] if v is not None}
        return await self.dao.find_all(limit, offset, order_by, **filter_by)

    async def del_article(self, article_id, user_id):
        article = await self.dao.find_one_or_none(id=article_id)
        if not article:
            raise ArticleNotFoundException
        if article.author_id != user_id:
            raise UserRightsException
        await self.dao.delete(id=article_id)

    async def set_type(self, article_id:int, article_type:str, user: Users):
        article = await self.dao.find_one_or_none(id=article_id)
        if not article:
            raise ArticleNotFoundException
        if not (article.author_id == user.id or user.status == "Admin"):
            raise UserRightsException
        edited_article = await self.dao.update(article.id, type=article_type)
        return edited_article


articles_service = ArticlesService()
