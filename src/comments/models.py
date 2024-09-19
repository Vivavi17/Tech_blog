"""Модуль с моделью таблицы комментариев"""

from sqlalchemy.orm import Mapped, relationship

from src.base.mixin_feedback_models import FeedbackMixin
from src.database import Base


class Comments(FeedbackMixin, Base):  # pylint: disable=too-few-public-methods
    """Модель контекста комментариев"""

    __tablename__ = "comments"

    article: Mapped["Articles"] = relationship("Articles", back_populates="comments")
