from datetime import datetime
from pydantic import BaseModel


class ORMBase(BaseModel):
    class Config:
        from_attributes = True


class TimestampOut(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None
