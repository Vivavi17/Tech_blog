from fastapi import APIRouter, Depends

from src.complaints.schemas import NewComplaintS
from src.users.models import Users

complaints_router = APIRouter(prefix="/complaints", tags=["complaints"])


@complaints_router.get("")
async def get_complaints(admin: Users = Depends()):
    return


@complaints_router.post("/{article_id}")
async def add_complaint(data: NewComplaintS, user: Users = Depends()):
    return
