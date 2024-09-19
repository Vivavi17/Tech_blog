"""Модуль запросов к таблице Reviews"""

from src.base.base_dao import BaseDAO
from src.reviews.models import Reviews


class ReviewsDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс для работы с таблицей отзывов"""

    model = Reviews
