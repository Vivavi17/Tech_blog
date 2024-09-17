from src.comments.dao import CommentsDAO


class CommentsService:
    singleton = None
    dao = CommentsDAO

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton

    async def add_new_comment(self, user_id: int, article_id: int, description: str):
        return await self.dao.add(
            author_id=user_id, article_id=article_id, description=description
        )

    async def del_comment(self, comment_id: int) -> None:
        return await self.dao.delete(id=comment_id)


comments_service = CommentsService()
