from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"agent": "Evaluator Agent", "status": "active"}
