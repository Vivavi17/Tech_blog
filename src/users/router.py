from fastapi import APIRouter, Depends

from src.users.models import Users
from src.users.schemas import UsersAuthS, UsersLoginS

router = APIRouter(prefix="/users", tags=['users'])


@router.post("/register", status_code=201)
async def register(data: UsersAuthS):
    return


@router.post("/login")
async def login(data: UsersLoginS):
    return


@router.post("/admins/{user_id}")
async def set_staus(user_id: int, admin: Users = Depends()):
    return


@router.post("/ban/{user_id}")
async def set_ban(user_id: int, ban=bool, admin: Users = Depends()):
    return
