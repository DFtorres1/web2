
from pydantic import UUID4, BaseModel


class ReviewsBase(BaseModel):
    rating: str
    description: str
    user_id: UUID4

class GetReviews(ReviewsBase):
    id: UUID4
    date_rating: str

class AddReviews(ReviewsBase):
    activity_id: str
    date_rating: str
    