"""
agents/evaluator_agent/routes.py
--------------------------------
Routes for Evaluator Agent — handles auto-grading and answer evaluation.
"""

from fastapi import APIRouter, Form
from agents.evaluator_agent import service

router = APIRouter()

@router.get("/")
async def evaluator_root():
    return {"agent": "Evaluator Agent", "status": "active"}

@router.post("/evaluate")
async def evaluate_submission(syllabus: str = Form(...)):
    """
    Evaluates student responses automatically.
    """
    data = service.evaluate_responses(syllabus)
    return {"status": "success", "data": data}
