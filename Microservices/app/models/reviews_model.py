import uuid
from sqlalchemy import Column, Date, Float, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from config.DB.db import Base



class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    rating = Column(Float, index=True, nullable=False)
    date_rating = Column(Date, index=True, nullable=False)
    description = Column(String, index=True)
    user_id = Column(String, index=True, nullable=False)
    activity_id = Column(Uuid, ForeignKey("activity.id"))

    activity = relationship("Activity", back_populates="reviews")