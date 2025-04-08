import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from config.DB.db import Base



class Favorites(Base):
    __tablename__ = "favorites"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    favorite_type = Column(String, index=True, nullable=False)
    date_added = Column(Date, index=True, nullable=False)
    activity_id = Column(Uuid, ForeignKey("activity.id"))

    activity = relationship("Activity", back_populates="favorites")