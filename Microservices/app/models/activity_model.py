import uuid
from sqlalchemy import Column, Integer, String, Uuid
from sqlalchemy.orm import relationship
from config.DB.db import Base

from models.favorite_model import Favorites
from models.reservation_model import Reservation
from models.reviews_model import Reviews

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    description = Column(String, unique=True, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    price = Column(Integer, nullable=False)
    availability = Column(String, nullable=False)

    reservation = relationship("Reservation", back_populates="activity")
    favorites = relationship("Favorites", back_populates="activity")
    reviews = relationship("Reviews", back_populates="activity")