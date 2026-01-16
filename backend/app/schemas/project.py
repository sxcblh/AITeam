from pydantic import BaseModel, Field

from app.schemas.common import ORMBase, TimestampOut


class ProjectCreate(BaseModel):
    key: str = Field(..., max_length=32)
    name: str = Field(..., max_length=128)
    description: str = ""


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class ProjectOut(ORMBase, TimestampOut):
    id: int
    key: str
    name: str
    description: str
