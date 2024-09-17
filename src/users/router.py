from fastapi import APIRouter, Depends, Response

from src.users.dependencies import check_admin
from src.users.models import Users
from src.users.schemas import UsersAuthS, UsersLoginS
from src.users.service import users_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", status_code=201)
async def register(data: UsersAuthS):
    """Создание учетной записи пользователя"""
    return await users_service.register(data.username, data.email, data.hashed_password)


@router.post("/login")
async def login(response: Response, data: UsersLoginS) -> str:
    """Вход пользователя по логину и паролю, пользователь получает токен доступа"""
    return await users_service.login(response, data.email, data.hashed_password)


@router.post("/admins/{user_id}")
async def set_status(user_id: int, admin: Users = Depends(check_admin)) -> None:
    """Изменить статус пользователя, по дефолту только сделать админом"""
    return await users_service.set_status(user_id, status="Admin", admin=admin)


@router.post("/ban/{user_id}")
async def set_ban(user_id: int, ban: bool, admin: Users = Depends(check_admin)):
    """Забанить/разбанить пользователя"""
    return await users_service.set_ban(user_id, ban)


@router.post("/logout")
async def logout(response: Response):
    """Выйти из учетной записи"""
    return await users_service.logout(response)
