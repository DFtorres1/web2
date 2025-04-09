from uuid import UUID
from sqlalchemy.orm import Session

from models.reviews_model import Reviews
from schemas.reviews import AddReviews, ReviewsBase


def get(id: UUID, db: Session):
    return db.query(Reviews).filter(id == id).first()


def create(activity_id: UUID, review: AddReviews, db: Session):
    new_review = Reviews(
        rating=review.rating,
        date_rating=review.date_rating,
        description=review.description,
        user_id=review.user_id,
        activity_id=activity_id
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


def get_all_reviews(db: Session):
    return db.query(Reviews).all()