"""Модуль запросов к таблице Reviews"""

from src.common.base_dao import BaseDAO
from src.reviews.models import Reviews


class ReviewsDAO(BaseDAO):
    """Класс для работы с таблицей отзывов"""

    model = Reviews
