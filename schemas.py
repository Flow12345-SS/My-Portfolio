# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    tech_stack: Optional[str] = None
    link: Optional[str] = None
    featured: Optional[bool] = False

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    image_filename: Optional[str] = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
