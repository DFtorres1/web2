from sqlite3 import IntegrityError
from sqlalchemy.orm import Session
from models.activity_model import Activity
from schemas.activity import ActivityBase

def create_activity(activity: ActivityBase, db: Session):
    new_activity = Activity(
        title = activity.title,
        description = activity.description,
        location = activity.location,
        price = activity.price,
        availability = activity.availability
    )
    try:
        db.add(new_activity)
        db.commit()
        db.refresh(new_activity)
        return new_activity
    except IntegrityError:
        db.rollback()
        raise ValueError("An activity with this description already exists.")



def get_all_activities(db: Session):
    return db.query(Activity).all()

def filter_activities(db: Session, title: str = None, price: int = None):
    query = db.query(Activity)
    if title:
        query = query.filter(Activity.title.ilike(f"%{title}%"))
    if price:
        query = query.filter(Activity.price == price)

    return query.all()