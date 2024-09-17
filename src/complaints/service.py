from typing import Optional

from src.complaints.dao import ComplaintsDAO


class ComplaintsService:
    singleton = None
    dao = ComplaintsDAO

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton

    async def get_complaints(
        self,
        article_id: Optional[int],
        author_id: Optional[int],
        limit: int,
        offset: int,
        order_by: str,
    ):
        filter_by = {
            k: v
            for k, v in [["article_id", article_id], ["author_id", author_id]]
            if v is not None
        }
        return await self.dao.find_all(limit, offset, order_by, **filter_by)

    async def add_new_complaint(self, user_id: int, article_id: int, description: str):
        return await self.dao.add(
            author_id=user_id, article_id=article_id, description=description
        )


complaints_service = ComplaintsService()
