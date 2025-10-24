"""
agents/exam_agent/routes.py
---------------------------
Routes for Exam Agent — supports web uploads and question generation.
"""

from fastapi import APIRouter, File, UploadFile, Form
from agents.exam_agent import service

router = APIRouter()

@router.post("/generate")
async def generate_exams(topics: str = Form(...)):
    """
    Generate smart, non-repetitive questions from topic list.
    """
    topic_list = [t.strip() for t in topics.split(",")]
    data = service.create_assessments({"topics": topic_list})
    return {"status": "success", "data": data}

@router.post("/upload")
async def upload_question_bank(file: UploadFile = File(...)):
    """
    Upload question bank files (.csv / .docx) for reference generation.
    """
    try:
        text = service.upload_and_parse(file)
        topics = text.split("\n")[:5]
        data = service.create_assessments({"topics": topics})
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
