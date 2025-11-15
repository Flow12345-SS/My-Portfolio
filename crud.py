# backend/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

def get_projects(db: Session, skip: int = 0, limit: int = 100) -> List[models.Project]:
    return db.query(models.Project).offset(skip).limit(limit).all()

def get_project(db: Session, project_id: int) -> Optional[models.Project]:
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def create_project(db: Session, project: schemas.ProjectCreate, image_filename: Optional[str] = None):
    db_proj = models.Project(**project.dict(), image_filename=image_filename)
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj

def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate, image_filename: Optional[str] = None):
    db_proj = get_project(db, project_id)
    if not db_proj:
        return None
    for k,v in project.dict(exclude_unset=True).items():
        setattr(db_proj, k, v)
    if image_filename:
        db_proj.image_filename = image_filename
    db.commit()
    db.refresh(db_proj)
    return db_proj

def delete_project(db: Session, project_id: int):
    db_proj = get_project(db, project_id)
    if not db_proj:
        return False
    db.delete(db_proj)
    db.commit()
    return True
