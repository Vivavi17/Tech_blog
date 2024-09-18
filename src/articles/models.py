"""Модель для работы со статьями"""

import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.comments.models import Comments
from src.complaints.models import Complaints
from src.database import Base
from src.reviews.models import Reviews


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
    comments: Mapped["Comments"] = relationship(
        "Comments", back_populates="article", cascade="all, delete-orphan"
    )
    complaints: Mapped["Complaints"] = relationship(
        "Complaints", back_populates="article", cascade="all, delete-orphan"
    )
    reviews: Mapped["Reviews"] = relationship(
        "Reviews", back_populates="article", cascade="all, delete-orphan"
    )
