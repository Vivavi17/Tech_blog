from src.comments.models import Comments
from src.common.base_dao import BaseDAO


class CommentsDAO(BaseDAO):
    model = Comments
