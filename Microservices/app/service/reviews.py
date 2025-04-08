from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session
from models.reviews_model import Reviews
from repositories.reviews_repository import create, get
from schemas.reviews import ReviewsBase
from datetime import date


def get_review(id: UUID, db: Session) -> Reviews:
    review = get(id, db)
    if not review:
        raise HTTPException(status_code=404, detail="No activities found")
    return review


def add_review(activity_id: UUID, review: ReviewsBase, db: Session):
    try:
        new_review = Reviews(
        rating=review.rating,
        date_rating=date.today(),
        description=review.description,
        user_id=review.user_id,
        activity_id=activity_id
    )
        create(activity_id, new_review, db)
        return {"message": "Review added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding review: {str(e)}")
