from fastapi import APIRouter

from app.api.v1.endpoints import auth, projects, requirements, bugs, releases, gitlab_webhooks

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(requirements.router, prefix="/requirements", tags=["requirements"])
api_router.include_router(bugs.router, prefix="/bugs", tags=["bugs"])
api_router.include_router(releases.router, prefix="/releases", tags=["releases"])
api_router.include_router(gitlab_webhooks.router, prefix="/webhooks", tags=["webhooks"])
