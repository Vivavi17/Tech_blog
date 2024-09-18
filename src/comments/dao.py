"""Модуль для работы с таблицей комментариев"""

from src.comments.models import Comments
from src.common.base_dao import BaseDAO


class CommentsDAO(BaseDAO):
    """Класс для работы с таблицей комментариев"""

    model = Comments
