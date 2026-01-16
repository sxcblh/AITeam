from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.requirement import Requirement
from app.schemas.requirement import RequirementCreate, RequirementOut, RequirementUpdate

router = APIRouter()


@router.get("/", response_model=list[RequirementOut])
def list_requirements(project_id: int | None = None, db: Session = Depends(get_db), _=Depends(get_current_user)):
    stmt = select(Requirement).order_by(Requirement.id.desc())
    if project_id is not None:
        stmt = stmt.where(Requirement.project_id == project_id)
    rows = db.execute(stmt).scalars().all()
    return rows


@router.post("/", response_model=RequirementOut)
def create_requirement(payload: RequirementCreate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = Requirement(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.patch("/{req_id}", response_model=RequirementOut)
def update_requirement(req_id: int, payload: RequirementUpdate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = db.get(Requirement, req_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Requirement not found")

    for k, v in payload.model_dump(exclude_none=True).items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{req_id}")
def delete_requirement(req_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    obj = db.get(Requirement, req_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Requirement not found")

    db.delete(obj)
    db.commit()
    return {"deleted": True}
