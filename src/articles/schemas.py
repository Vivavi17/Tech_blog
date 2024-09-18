"""Модуль со схемами валидации статей"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewArticleS(BaseModel):
    """Валидация при создании новой статьи"""

    type: str
    description: str


class ArticlesS(BaseModel):
    """Валидация отправки статей"""

    id: int
    type: str
    description: str
    created_at: datetime


class ArticlesFilterS(BaseModel):
    """Валидация фильтров на статью"""

    author_id: Optional[int]
    type: Optional[str]
