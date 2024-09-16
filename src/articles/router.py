from fastapi import APIRouter, Depends

from src.articles.schemas import NewArticleS, ArticlesS, NewCommentS, NewComplaintS, NewReviewsS
from src.users.models import Users

articles_router = APIRouter(prefix="/articles", tags=['articles'])
comments_router = APIRouter(prefix="/comments", tags=['comments'])
complaints_router = APIRouter(prefix="/complaints", tags=['complaints'])
reviews_router = APIRouter(prefix="/reviews", tags=['reviews'])


@articles_router.post("")
async def add_new_article(data: NewArticleS, user=Depends()):
    return


@articles_router.get("")
async def get_articles(limit: int = 5, offset: int = 0) -> list[ArticlesS]:
    return


@articles_router.get("/{article_id}")
async def get_article(article_id: int) -> ArticlesS:
    return


@articles_router.delete("/{article_id}")
async def del_article(article_id: int, user: Users = Depends()) -> ArticlesS:
    return


@articles_router.patch("/{article_id}")
async def set_type(article_id: int, article_type: str):
    return


@comments_router.post("/{article_id}")
async def add_comment(article_id: int, data: NewCommentS, user: Users = Depends()):
    return


@comments_router.delete("/{comment_id}")
async def del_article(comment_id: int, admin: Users =Depends()):
    return


@complaints_router.get("")
async def get_complaints(admin: Users =Depends()):
    return


@complaints_router.post("/{article_id}")
async def add_complaint(data: NewComplaintS, user: Users =Depends()):
    return


@reviews_router.post("/{article_id}")
async def add_review(data: NewReviewsS, user=Depends()):
    return
