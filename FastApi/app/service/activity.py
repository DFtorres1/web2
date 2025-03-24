from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.activity_repository import create_activity, filter_activities, get_all_activities
from schemas.activity import ActivityBase, GetActivity


def create(db: Session, activity: ActivityBase):
    try:
        return create_activity(activity=activity, db=db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating activity: {str(e)}")


def get_activity(db: Session) -> list[GetActivity]:
    activities = get_all_activities(db=db)
    if not activities:
        raise HTTPException(status_code=404, detail="No activities found")
    return activities


def filter_activity_service(db: Session, title: str = None, price: int = None):
    activities = filter_activities(db=db, title=title, price=price)
    if not activities:
        raise HTTPException(status_code=404, detail="No activities found")
    return activities