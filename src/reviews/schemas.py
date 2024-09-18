"""Модуль со схемами валидации отзывов"""

from pydantic import BaseModel


class NewReviewsS(BaseModel):
    """Валидация при добавлении нового отзыва"""

    description: str


class ReviewsS(BaseModel):
    """Валидация отзыва"""

    author_id: int
    article_id: int
    description: str
