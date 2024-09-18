"""Модуль схем валидации жалоб"""

from pydantic import BaseModel


class NewComplaintS(BaseModel):
    """Валидация при создании жалоб"""

    description: str


class ComplaintS(BaseModel):
    """Валидация при просмотре жалоб"""

    author_id: int
    article_id: int
    description: str
