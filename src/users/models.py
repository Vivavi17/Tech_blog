"""Модель для работы с пользователями"""

from typing import Literal

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Users(Base):  # pylint: disable=too-few-public-methods
    """Модель контекста пользователя"""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str]
    hashed_password: Mapped[str]
    status: Mapped[Literal["User", "Admin"]] = mapped_column(default="User")
    ban: Mapped[bool] = mapped_column(default=False)
