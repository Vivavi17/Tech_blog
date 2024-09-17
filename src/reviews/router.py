from fastapi import APIRouter, Depends

from src.articles.schemas import NewReviewsS

reviews_router = APIRouter(prefix="/reviews", tags=['reviews'])


@reviews_router.post("/{article_id}")
async def add_review(data: NewReviewsS, user=Depends()):
    return
