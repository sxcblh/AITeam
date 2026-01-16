from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.release import Release
from app.schemas.release import ReleaseCreate, ReleaseOut, ReleaseUpdate

router = APIRouter()


@router.get("/", response_model=list[ReleaseOut])
def list_releases(project_id: int | None = None, db: Session = Depends(get_db), _=Depends(get_current_user)):
    stmt = select(Release).order_by(Release.id.desc())
    if project_id is not None:
        stmt = stmt.where(Release.project_id == project_id)
    rows = db.execute(stmt).scalars().all()
    return rows


@router.post("/", response_model=ReleaseOut)
def create_release(payload: ReleaseCreate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = Release(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.patch("/{release_id}", response_model=ReleaseOut)
def update_release(release_id: int, payload: ReleaseUpdate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = db.get(Release, release_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Release not found")

    for k, v in payload.model_dump(exclude_none=True).items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{release_id}")
def delete_release(release_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = db.get(Release, release_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Release not found")

    db.delete(obj)
    db.commit()
    return {"deleted": True}
