import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Comments(Base):
    """Модель контекста комментариев"""

    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
    description: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
