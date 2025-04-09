from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session

from config.DB.db import SessionLocal
from schemas.reviews import ReviewsBase
from service.reviews import add_review, get_review

reviews = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@reviews.get('/reviews/{id}', tags=['Reviews'])
def read_review(id: UUID, db: Session = Depends(get_db) ):
    return JSONResponse(content=jsonable_encoder({'review':get_review(id, db)}))

@reviews.post('/review/{activity_id}', tags=['Reviews'], status_code=201)
def create_review(activity_id: UUID, review: ReviewsBase, db: Session = Depends(get_db)):
    print('HOLAAA', review)
    return add_review(activity_id, review, db)