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

## Delivery Workflow (Boss-Driven)
- Boss provides a fuzzy goal; PM coordinates with Customer (product) and RD Lead to clarify requirements and feasibility, then outputs PRD/SRS/Acceptance plus a decision pack with dev + test plans.
- Boss approval is required before any implementation; no coding starts without a clear YES.
- After `/prompts:boss`, auto-run the next command(s) unless a boss decision is explicitly required.
- After approval, RD Lead leads Architect/Engineer/Algorithm/UI with explicit task ownership and acceptance criteria.
- Development must pass Build Gate then UnitTest Gate; if any gate fails, return to dev and repeat.
- QA runs only after build + unit tests pass; QA uses mouse/keyboard automation, captures screenshots/logs, and files bugs back to dev.
- Bugfix loop continues until QA passes; only then is the task considered complete.
