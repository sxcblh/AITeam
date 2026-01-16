"""init

Revision ID: 0001
Revises: 
Create Date: 2026-01-16

"""

from alembic import op
import sqlalchemy as sa


revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("key", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("description", sa.Text(), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )
    op.create_index("ix_projects_key", "projects", ["key"], unique=True)
    op.create_index("ix_projects_name", "projects", ["name"])

    op.create_table(
        "requirements",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("project_id", sa.Integer(), sa.ForeignKey("projects.id"), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=False, server_default=""),
        sa.Column("status", sa.String(length=32), nullable=False, server_default="Draft"),
        sa.Column("priority", sa.Integer(), nullable=False, server_default="3"),
        sa.Column("assignee", sa.String(length=64), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )
    op.create_index("ix_requirements_project_id", "requirements", ["project_id"])
    op.create_index("ix_requirements_title", "requirements", ["title"])
    op.create_index("ix_requirements_status", "requirements", ["status"])

    op.create_table(
        "bugs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("project_id", sa.Integer(), sa.ForeignKey("projects.id"), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=False, server_default=""),
        sa.Column("status", sa.String(length=32), nullable=False, server_default="New"),
        sa.Column("severity", sa.Integer(), nullable=False, server_default="3"),
        sa.Column("assignee", sa.String(length=64), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )
    op.create_index("ix_bugs_project_id", "bugs", ["project_id"])
    op.create_index("ix_bugs_title", "bugs", ["title"])
    op.create_index("ix_bugs_status", "bugs", ["status"])

    op.create_table(
        "releases",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("project_id", sa.Integer(), sa.ForeignKey("projects.id"), nullable=False),
        sa.Column("version", sa.String(length=32), nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False, server_default=""),
        sa.Column("notes", sa.Text(), nullable=False, server_default=""),
        sa.Column("status", sa.String(length=32), nullable=False, server_default="Planning"),
        sa.Column("build_no", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )
    op.create_index("ix_releases_project_id", "releases", ["project_id"])
    op.create_index("ix_releases_version", "releases", ["version"])
    op.create_index("ix_releases_status", "releases", ["status"])

    op.create_table(
        "gitlab_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("event_type", sa.String(length=64), nullable=False),
        sa.Column("event_id", sa.String(length=128), nullable=False, server_default=""),
        sa.Column("project_key", sa.String(length=64), nullable=False, server_default=""),
        sa.Column("raw_json", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )
    op.create_index("ix_gitlab_events_event_type", "gitlab_events", ["event_type"])
    op.create_index("ix_gitlab_events_event_id", "gitlab_events", ["event_id"])
    op.create_index("ix_gitlab_events_project_key", "gitlab_events", ["project_key"])


def downgrade() -> None:
    op.drop_table("gitlab_events")
    op.drop_table("releases")
    op.drop_table("bugs")
    op.drop_table("requirements")
    op.drop_table("projects")
