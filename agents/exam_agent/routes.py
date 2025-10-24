"""
agents/exam_agent/routes.py
---------------------------
Routes for Exam Agent — handles question paper and quiz generation.
"""

from fastapi import APIRouter, Form
from agents.exam_agent import service

router = APIRouter()

@router.get("/")
async def exam_root():
    return {"agent": "Exam Agent", "status": "active"}

@router.post("/create")
async def create_exam(syllabus: str = Form(...)):
    """
    Generates exam questions and assignments based on syllabus.
    """
    data = service.generate_exam(syllabus)
    return {"status": "success", "data": data}
