# backend/app/models.py
from sqlalchemy import Column, Integer, String, Text, Boolean
from .database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    tech_stack = Column(String(200), nullable=True)
    image_filename = Column(String(300), nullable=True)
    link = Column(String(300), nullable=True)   # project link (github/demo)
    featured = Column(Boolean, default=False)
