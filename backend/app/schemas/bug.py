from pydantic import BaseModel, Field

from app.schemas.common import ORMBase, TimestampOut


class BugCreate(BaseModel):
    project_id: int
    title: str = Field(..., max_length=256)
    description: str = ""
    status: str = "New"
    severity: int = 3
    assignee: str = ""


class BugUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    severity: int | None = None
    assignee: str | None = None


class BugOut(ORMBase, TimestampOut):
    id: int
    project_id: int
    title: str
    description: str
    status: str
    severity: int
    assignee: str
