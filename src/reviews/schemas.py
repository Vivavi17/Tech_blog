from pydantic import BaseModel


class NewReviewsS(BaseModel):
    article_id: int
    description: str
