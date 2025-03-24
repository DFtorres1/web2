from pydantic import BaseModel, UUID4
from typing import List, Optional

class ActivityBase(BaseModel):
    title: str
    description: str
    location: str
    price: int
    availability: str

class GetActivity(ActivityBase):
    id: UUID4

    class Config:
        from_attributes = True 
