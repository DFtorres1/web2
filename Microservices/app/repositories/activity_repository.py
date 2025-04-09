from sqlite3 import IntegrityError
from uuid import UUID
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


def delete_activity(id: UUID, db: Session):
    activity = db.query(Activity).filter(Activity.id == id).first()
    if activity:
        db.delete(activity)
        db.commit()
    else:
        raise ValueError("Activity not found.")
    

def update_activity(id: UUID, db: Session, activity: ActivityBase):
    activity_to_update = db.query(Activity).filter(Activity.id == id).first()
    
    if not activity_to_update:
        raise ValueError("Activity not found.")

    for key, value in activity.dict().items():
        setattr(activity_to_update, key, value)

    db.commit()
    db.refresh(activity_to_update)
    return activity_to_update