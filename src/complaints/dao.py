"""Модуль с запросами к таблице жалоб"""

from src.base.base_dao import BaseDAO
from src.complaints.models import Complaints


class ComplaintsDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс для работы с таблицей жалоб"""

    model = Complaints
