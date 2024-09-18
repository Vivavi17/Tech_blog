"""Схемы валидации пользователей"""

from pydantic import BaseModel, EmailStr, Field


class UsersLoginS(BaseModel):
    """Валидация для входа в учетную запись"""

    email: EmailStr
    password: str


class UsersAuthS(UsersLoginS, BaseModel):
    """Валидация регистрации пользователя"""

    username: str = Field(max_length=20)
