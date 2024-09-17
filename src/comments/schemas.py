from pydantic import BaseModel


class NewCommentS(BaseModel):
    description: str


class CommentS(BaseModel):
    author_id: int
    article_id: int
    description: str
