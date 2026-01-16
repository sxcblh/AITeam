from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.common import TimestampMixin


class Bug(Base, TimestampMixin):
    __tablename__ = "bugs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), index=True)

    title: Mapped[str] = mapped_column(String(256), index=True)
    description: Mapped[str] = mapped_column(Text, default="")

    # New/Triage/Assigned/Fixing/Merged/Verified/Released/Closed
    status: Mapped[str] = mapped_column(String(32), default="New", index=True)

    severity: Mapped[int] = mapped_column(Integer, default=3)  # 1 critical, 5 minor
    assignee: Mapped[str] = mapped_column(String(64), default="")
