<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

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