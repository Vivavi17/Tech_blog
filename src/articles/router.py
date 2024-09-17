from typing import Literal, Optional

from fastapi import APIRouter, Depends

from src.articles.schemas import ArticlesS, NewArticleS
from src.articles.service import articles_service
from src.users.dependencies import check_admin, check_user
from src.users.models import Users

articles_router = APIRouter(prefix="/articles", tags=["articles"])


@articles_router.post("")
async def add_new_article(
    data: NewArticleS, user: Users = Depends(check_user)
) -> ArticlesS:
    return await articles_service.add_new_article(user.id, data.type, data.description)


@articles_router.get("")
async def get_articles(
    articles_type: Optional[str] = None,
    author_id: Optional[str] = None,
    order_by: Optional[Literal["author_id", "type", "crated_at"]] = None,
    limit: int = 5,
    offset: int = 0,
    user: Users = Depends(check_user),
) -> list[ArticlesS]:
    return await articles_service.get_articles(
        articles_type, author_id, limit, offset, order_by
    )


@articles_router.get("/{article_id}")
async def get_article(
    article_id: int, user: Users = Depends(check_user)
) -> Optional[ArticlesS]:
    return await articles_service.get_article(article_id)


@articles_router.delete("/{article_id}")
async def del_article(article_id: int, user: Users = Depends(check_user)) -> None:
    return await articles_service.del_article(article_id, user.id)


@articles_router.patch("/{article_id}")
async def set_type(
    article_id: int, article_type: str, user: Users = Depends(check_user)
) -> ArticlesS:
    return articles_service.set_type(article_id, article_type, user)
