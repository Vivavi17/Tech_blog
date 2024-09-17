from pydantic import BaseModel


class NewComplaintS(BaseModel):
    description: str


class ComplaintS(BaseModel):
    author_id: int
    article_id: int
    description: str
