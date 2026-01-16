from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.common import TimestampMixin


class GitlabEvent(Base, TimestampMixin):
    __tablename__ = "gitlab_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    event_type: Mapped[str] = mapped_column(String(64), index=True)
    event_id: Mapped[str] = mapped_column(String(128), default="", index=True)
    project_key: Mapped[str] = mapped_column(String(64), default="", index=True)

    raw_json: Mapped[str] = mapped_column(Text)  # store original payload
