from pydantic import BaseModel, Field

from app.schemas.common import ORMBase, TimestampOut


class RequirementCreate(BaseModel):
    project_id: int
    title: str = Field(..., max_length=256)
    description: str = ""
    status: str = "Draft"
    priority: int = 3
    assignee: str = ""


class RequirementUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: int | None = None
    assignee: str | None = None


class RequirementOut(ORMBase, TimestampOut):
    id: int
    project_id: int
    title: str
    description: str
    status: str
    priority: int
    assignee: str
