from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.bug import Bug
from app.schemas.bug import BugCreate, BugOut, BugUpdate

router = APIRouter()


@router.get("/", response_model=list[BugOut])
def list_bugs(project_id: int | None = None, db: Session = Depends(get_db), _=Depends(get_current_user)):
    stmt = select(Bug).order_by(Bug.id.desc())
    if project_id is not None:
        stmt = stmt.where(Bug.project_id == project_id)
    rows = db.execute(stmt).scalars().all()
    return rows


@router.post("/", response_model=BugOut)
def create_bug(payload: BugCreate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = Bug(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.patch("/{bug_id}", response_model=BugOut)
def update_bug(bug_id: int, payload: BugUpdate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = db.get(Bug, bug_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Bug not found")

    for k, v in payload.model_dump(exclude_none=True).items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{bug_id}")
def delete_bug(bug_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = db.get(Bug, bug_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Bug not found")

    db.delete(obj)
    db.commit()
    return {"deleted": True}
