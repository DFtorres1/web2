import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from config.DB.db import Base


class Reservation(Base):
    __tablename__ = "info"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    reservation_date = Column(Date, index=True, nullable=False)
    status = Column(String, index=True, nullable=False)
    activity_id = Column(Uuid, ForeignKey("activity.id"))

    activity = relationship("Activity", back_populates="reservation")