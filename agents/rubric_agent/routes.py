"""
agents/rubric_agent/routes.py
-----------------------------
Routes for Rubric Agent — defines evaluation criteria for assignments and exams.
"""

from fastapi import APIRouter, Form
from agents.rubric_agent import service

router = APIRouter()

@router.get("/")
async def rubric_root():
    return {"agent": "Rubric Agent", "status": "active"}

@router.post("/design")
async def design_rubric(syllabus: str = Form(...)):
    """
    Designs grading and evaluation rubrics for syllabus topics.
    """
    data = service.design_rubric(syllabus)
    return {"status": "success", "data": data}
