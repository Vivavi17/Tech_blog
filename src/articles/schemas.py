from datetime import datetime

from pydantic import BaseModel

class NewArticleS(BaseModel):
    author_id: int
    type: str
    description: str

class ArticlesS(BaseModel):
    type: str
    description: str
    created_at: datetime


class NewCommentS(BaseModel):
    article_id: int
    description: str

class NewComplaintS(BaseModel):
    article_id: int
    description: str

class NewReviewsS(BaseModel):
    article_id: int
    description: str