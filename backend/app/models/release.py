from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.common import TimestampMixin


class Release(Base, TimestampMixin):
    __tablename__ = "releases"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), index=True)

    version: Mapped[str] = mapped_column(String(32), index=True)
    title: Mapped[str] = mapped_column(String(128), default="")
    notes: Mapped[str] = mapped_column(Text, default="")

    # Planning/BuildReady/Testing/Approval/Deploying/Released/RolledBack
    status: Mapped[str] = mapped_column(String(32), default="Planning", index=True)

    build_no: Mapped[int] = mapped_column(Integer, default=0)
