"""модуль для работы с таблицей статей"""

from src.articles.models import Articles
from src.base.base_dao import BaseDAO


class ArticlesDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс с запросами в таблицу статей"""

    model = Articles
