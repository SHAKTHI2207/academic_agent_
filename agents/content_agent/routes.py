from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"agent": "Content Agent", "status": "active"}
