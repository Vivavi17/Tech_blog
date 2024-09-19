"""Модуль с моделью таблицы отзывов"""

from sqlalchemy.orm import Mapped, relationship

from src.base.mixin_feedback_models import FeedbackMixin
from src.database import Base


class Reviews(FeedbackMixin, Base):  # pylint: disable=too-few-public-methods
    """Модель контекста отзывов"""

    __tablename__ = "reviews"

    article: Mapped["Articles"] = relationship(back_populates="reviews")
