from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"agent": "Analytics Agent", "status": "active"}
