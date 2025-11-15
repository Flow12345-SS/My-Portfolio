from fastapi import APIRouter

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("/")
def get_projects():
    return [
        {"id": 1, "name": "AI Plant Disease Detection", "tech": "Python, CNN"},
        {"id": 2, "name": "Portfolio Website", "tech": "React, FastAPI"},
        {"id": 3, "name": "Grey Water Management", "tech": "ML + IoT"},
    ]
