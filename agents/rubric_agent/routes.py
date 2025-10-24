from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"agent": "Rubric Agent", "status": "active"}
