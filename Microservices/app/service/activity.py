from fastapi import HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from repositories.activity_repository import create_activity, delete_activity, filter_activities, get_all_activities, update_activity
from repositories.reviews_repository import get_all_reviews
from schemas.activity import ActivityBase, GetActivity
import pandas as pd

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

def delete(id: UUID, db: Session):
    try:
        delete_activity(id=id, db=db)
        return {"message": "Activity deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting activity: {str(e)}")
    
def update(id: UUID, db: Session, activity: ActivityBase):
    try:
        return update_activity(id=id, db=db, activity=activity)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating activity: {str(e)}")
    


def relevant(db: Session):
    activities = get_all_activities(db)
    reviews = get_all_reviews(db)

    # Convertimos las reviews a DataFrame
    df_reviews = pd.DataFrame([
        {"activity_id": review.activity_id, "rating": review.rating}
        for review in reviews
    ])

    if df_reviews.empty:
        return []

    # Agrupar por actividad y calcular métricas
    review_stats = df_reviews.groupby("activity_id").agg(
        average_rating=("rating", "mean"),
        review_count=("rating", "count")
    ).reset_index()

    # Ordenar primero por promedio de rating, luego por cantidad de reviews
    review_stats.sort_values(
        by=["average_rating", "review_count"], ascending=[False, False], inplace=True
    )

    # Obtener IDs de actividades ordenadas por relevancia
    sorted_ids = review_stats["activity_id"].tolist()

    # Mapeo de actividades por ID para acceso rápido
    activity_dict = {activity.id: activity for activity in activities}

    # Filtrar y ordenar actividades relevantes
    relevant_activities = [activity_dict[aid] for aid in sorted_ids if aid in activity_dict]

    return relevant_activities