"""Модуль роутрера complaints"""

from typing import Literal, Optional

from fastapi import APIRouter, Depends

from src.complaints.schemas import ComplaintS, NewComplaintS
from src.complaints.service import complaints_service
from src.users.dependencies import check_admin, check_user
from src.users.models import Users

complaints_router = APIRouter(prefix="/complaints", tags=["complaints"])


@complaints_router.get("", dependencies=[Depends(check_admin)])
async def get_complaints(
    article_id: Optional[str] = None,
    author_id: Optional[str] = None,
    order_by: Optional[Literal["author_id", "article_id", "crated_at"]] = None,
    limit: int = 5,
    offset: int = 0,
) -> list[ComplaintS]:
    """Получить список жалоб (для АДМ)"""
    return await complaints_service.get_complaints(
        article_id, author_id, limit, offset, order_by
    )


@complaints_router.post("/{article_id}")
async def add_complaint(
    article_id: int, data: NewComplaintS, user: Users = Depends(check_user)
) -> ComplaintS:
    """Добавить жалобу"""
    return await complaints_service.add_new_complaint(
        user.id, article_id, data.description
    )
