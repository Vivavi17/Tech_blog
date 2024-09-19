"""Модуль с моделью таблицы жалоб"""

from sqlalchemy.orm import Mapped, relationship

from src.base.mixin_feedback_models import FeedbackMixin
from src.database import Base


class Complaints(FeedbackMixin, Base):  # pylint: disable=too-few-public-methods
    """Модель контекста жалоб"""

    __tablename__ = "complaints"

    article: Mapped["Articles"] = relationship(back_populates="complaints")
