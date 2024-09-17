from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewArticleS(BaseModel):
    type: str
    description: str


class ArticlesS(BaseModel):
    type: str
    description: str
    created_at: datetime


class ArticlesFilterS(BaseModel):
    author_id: Optional[int]
    type: Optional[str]
