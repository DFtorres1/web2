from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uuid import UUID
from sqlalchemy.orm import Session
from typing import List, Optional
from config.DB.db import SessionLocal
from models.activity_model import Activity
from schemas.activity import ActivityBase, GetActivity
import asyncio
import nats

from service.activity import create, delete, filter_activity_service, get_activity, relevant, update


activity_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# async def get_nats_connection():
#     if not hasattr(get_nats_connection, "nc"):
#         get_nats_connection.nc = await nats.connect("nats://localhost:4222")
#     return get_nats_connection.nc


@activity_router.post('/activities', tags=['Activity'], response_model=ActivityBase, status_code=201)
def create_activity_post(activity: ActivityBase, db: Session = Depends(get_db)):
    return create(db=db, activity=activity)


@activity_router.get('/activities', tags=['Activity'], response_model=List[GetActivity], status_code=200)
def get_activities_list(db: Session = Depends(get_db)):
    return get_activity(db)


@activity_router.get('/activities-by', tags=['Activity'], response_model=List[GetActivity], status_code=200)
def filter_activities(db: Session = Depends(get_db), title: Optional[str] = Query(None), price: Optional[int] = Query(None)):
    return filter_activity_service(db=db, title=title, price=price)


@activity_router.delete('/activities/{id}', tags=['Activity'])
def delete_activity_by_id(id:UUID, db: Session = Depends(get_db)):
    return delete(id, db)


@activity_router.put('/activity/{id}', tags=['Activity'], response_model=ActivityBase, status_code=200)
def update_activity_by_id(id: UUID, activity: ActivityBase, db: Session = Depends(get_db)):
    return update(id=id, activity=activity, db=db)


@activity_router.get('/relevat_activity', tags=['Activity'], response_model=List[ActivityBase])
def get_relevat_activity(db: Session = Depends(get_db)):
    return JSONResponse(content=jsonable_encoder({'message':relevant(db)}))




@activity_router.post('/createActivities', tags=['Mala practica'], response_model=ActivityBase, status_code=201)
def create_activity(activity: ActivityBase, db: Session = Depends(get_db)):
    return create(db=db, activity=activity)

@activity_router.get('/activities-by-price/{price}', tags=['Mala practica'], response_model=List[ActivityBase], status_code=200)
def get_activities_by_price(price: int, db: Session = Depends(get_db)):
    return db.query(Activity).filter(Activity.price == price).all()

@activity_router.get('/activities-by-title/{title}', tags=['Mala practica'], response_model=List[ActivityBase], status_code=200)
def get_activities_by_title(title: str, db: Session = Depends(get_db)):
    return db.query(Activity).filter(Activity.title == title).all()

@activity_router.get('/getActivities', tags=['Mala practica'], response_model=List[GetActivity], status_code=200)
def get_activities(db: Session = Depends(get_db)):
    return get_activity(db)



# 🟢 Obtener actividades y enviarlas a NATS
# @activity_router.get('/activities_nats', tags=['Activity Nats'], status_code=200)
# async def get_activities_nats(db: Session = Depends(get_session)):
#     activities = db.query(Activity).all()
#     if not activities:
#         raise HTTPException(status_code=404, detail="No activities found")

#     data = {"activities": [activity.model_dump() for activity in activities]}
#     json_data = json.dumps(data)

#     # Publicar en NATS
#     nc = await get_nats_connection()
#     await nc.publish("activities", json_data.encode())

#     return {"message": "Data sent to NATS successfully"}

# # 🟢 Crear actividad y publicarla en NATS
# @activity_router.post('/create_activity', tags=['Activity'])
# async def create_activity(data: dict):
#     print("Recibido:", data)

#     # Publicar en NATS
#     nc = await get_nats_connection()
#     await nc.publish('activity.crear', json.dumps(data).encode())
#     return {'message': 'Activity created and sent to NATS'}
