from pydantic import BaseModel, Field

from app.schemas.common import ORMBase, TimestampOut


class ReleaseCreate(BaseModel):
    project_id: int
    version: str = Field(..., max_length=32)
    title: str = ""
    notes: str = ""
    status: str = "Planning"
    build_no: int = 0


class ReleaseUpdate(BaseModel):
    version: str | None = None
    title: str | None = None
    notes: str | None = None
    status: str | None = None
    build_no: int | None = None


class ReleaseOut(ORMBase, TimestampOut):
    id: int
    project_id: int
    version: str
    title: str
    notes: str
    status: str
    build_no: int
