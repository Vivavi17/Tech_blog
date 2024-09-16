"""Модель для работы со статьями"""

import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database import Base


class Articles(Base):
    """Модель контекста статей"""

    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    type: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class ColumnMixin:
    """Миксины столбцов жалоб, комментариев, отзывов"""

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
    description: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class Complaints(ColumnMixin, Base):
    """Модель контекста жалоб"""

    __tablename__ = "complaints"


class Comments(ColumnMixin, Base):
    """Модель контекста комментариев"""

    __tablename__ = "comments"


class Reviews(ColumnMixin, Base):
    """Модель контекста отзывов"""

    __tablename__ = "reviews"
