from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.common import TimestampMixin


class Requirement(Base, TimestampMixin):
    __tablename__ = "requirements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), index=True)

    title: Mapped[str] = mapped_column(String(256), index=True)
    description: Mapped[str] = mapped_column(Text, default="")

    # Draft/Review/Approved/InDev/InTest/Done/Archived
    status: Mapped[str] = mapped_column(String(32), default="Draft", index=True)

    priority: Mapped[int] = mapped_column(Integer, default=3)  # 1 high, 5 low
    assignee: Mapped[str] = mapped_column(String(64), default="")
