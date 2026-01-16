import hmac
import json

from fastapi import APIRouter, Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.gitlab_event import GitlabEvent

router = APIRouter()


def _verify_secret(secret: str, token: str | None):
    if not secret:
        return True
    if not token:
        return False
    # GitLab 的 Secret Token 直接对比即可
    return hmac.compare_digest(secret, token)


@router.post("/gitlab")
async def gitlab_webhook(
    request: Request,
    x_gitlab_event: str | None = Header(default=None, alias="X-Gitlab-Event"),
    x_gitlab_token: str | None = Header(default=None, alias="X-Gitlab-Token"),
    db: Session = Depends(get_db),
):
    if not _verify_secret(settings.gitlab_webhook_secret, x_gitlab_token):
        raise HTTPException(status_code=401, detail="Invalid webhook token")

    payload = await request.json()
    raw_json = json.dumps(payload, ensure_ascii=False)

    event_type = x_gitlab_event or payload.get("object_kind") or "unknown"
    event_id = str(payload.get("event_id") or payload.get("object_attributes", {}).get("id") or "")

    project = payload.get("project") or {}
    project_key = str(project.get("path_with_namespace") or project.get("path") or "")

    obj = GitlabEvent(event_type=event_type, event_id=event_id, project_key=project_key, raw_json=raw_json)
    db.add(obj)
    db.commit()

    return {"received": True, "event_type": event_type}
