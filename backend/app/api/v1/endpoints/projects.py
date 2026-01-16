from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.deps import get_current_user, require_role
from app.db.session import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectOut, ProjectUpdate

router = APIRouter()


@router.get("/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db), _=Depends(get_current_user)):
    rows = db.execute(select(Project).order_by(Project.id.desc())).scalars().all()
    return rows


@router.post("/", response_model=ProjectOut)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db), _=Depends(require_role("admin"))):
    exists = db.execute(select(Project).where(Project.key == payload.key)).scalar_one_or_none()
    if exists:
        raise HTTPException(status_code=400, detail="Project key already exists")

    obj = Project(key=payload.key, name=payload.name, description=payload.description)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.patch("/{project_id}", response_model=ProjectOut)
def update_project(project_id: int, payload: ProjectUpdate, db: Session = Depends(get_db), _=Depends(require_role("admin"))):
    obj = db.get(Project, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")

    if payload.name is not None:
        obj.name = payload.name
    if payload.description is not None:
        obj.description = payload.description

    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), _=Depends(require_role("admin"))):
    obj = db.get(Project, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(obj)
    db.commit()
    return {"deleted": True}
