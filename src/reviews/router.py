"""Модуль роутера отзывов"""

from fastapi import APIRouter, Depends

from src.reviews.schemas import NewReviewsS, ReviewsS
from src.reviews.service import reviews_service
from src.users.dependencies import check_user

reviews_router = APIRouter(prefix="/reviews", tags=["reviews"])


@reviews_router.post("/{article_id}")
async def add_review(
    article_id: int, data: NewReviewsS, user=Depends(check_user)
) -> ReviewsS:
    """Добавить отзыв нв статью"""
    return await reviews_service.add_review(user.id, article_id, data.description)
