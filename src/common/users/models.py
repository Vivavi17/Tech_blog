"""Модель для работы с пользователями"""

from typing import Literal

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.common.database import Base


class Users(Base):
    """Модель контекста пользователя"""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str]
    hashed_password: Mapped[str]
    status: Mapped[Literal["User", "Admin"]]
    ban: Mapped[bool]
