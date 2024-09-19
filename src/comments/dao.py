"""Модуль для работы с таблицей комментариев"""

from src.base.base_dao import BaseDAO
from src.comments.models import Comments


class CommentsDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс для работы с таблицей комментариев"""

    model = Comments
