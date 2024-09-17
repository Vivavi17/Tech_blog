from fastapi import APIRouter, Depends

from src.articles.schemas import NewCommentS
from src.users.models import Users

comments_router = APIRouter(prefix="/comments", tags=['comments'])


@comments_router.post("/{article_id}")
async def add_comment(article_id: int, data: NewCommentS, user: Users = Depends()):
    return


@comments_router.delete("/{comment_id}")
async def del_comments(comment_id: int, admin: Users =Depends()):
    return
