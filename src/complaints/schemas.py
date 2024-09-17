from pydantic import BaseModel


class NewComplaintS(BaseModel):
    article_id: int
    description: str
