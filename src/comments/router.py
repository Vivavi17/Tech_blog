"""Модуль роутера комментариев"""

from fastapi import APIRouter, Depends

from src.comments.schemas import CommentS, NewCommentS
from src.comments.service import comments_service
from src.users.dependencies import check_admin, check_user
from src.users.models import Users

comments_router = APIRouter(prefix="/comments", tags=["comments"])


@comments_router.post("/{article_id}")
async def add_comment(
    article_id: int, data: NewCommentS, user: Users = Depends(check_user)
) -> CommentS:
    """Добавить комментарий"""
    return await comments_service.add_new_comment(user.id, article_id, data.description)


@comments_router.delete("/{comment_id}", dependencies=[Depends(check_admin)])
async def del_comments(comment_id: int) -> None:
    """Удалить комментарий (админом)"""
    return await comments_service.del_comment(comment_id)
