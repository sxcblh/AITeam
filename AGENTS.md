# Repository Rules (for Codex / contributors)

## Tech
- Backend: FastAPI + SQLAlchemy 2.0 style
- DB: PostgreSQL
- Migrations: Alembic
- Auth: JWT
- Frontend: React + TypeScript (Vite)

## Conventions
- Add new API under backend/app/api/v1/endpoints
- For each new resource:
  - models/*.py
  - schemas/*.py
  - endpoints/*.py
  - add router in api/v1/router.py
  - add minimal unit tests (future)

## Safety
- Never run destructive commands (rm -rf /, dropdb, etc.)
- Always prefer idempotent migrations

## Commit format
[TASK-xxxx] <summary>