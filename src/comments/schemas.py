"""Модуль со схемами валидации комментариев"""

from pydantic import BaseModel


class NewCommentS(BaseModel):
    """Валидация на новый комментарий"""

    description: str


class CommentS(BaseModel):
    """Валидация на полуцчение комментариев"""

    author_id: int
    article_id: int
    description: str
