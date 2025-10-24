"""
agents/content_agent/routes.py
------------------------------
Routes for Content Agent — handles syllabus uploads and content generation.
"""

from fastapi import APIRouter, File, UploadFile, Form
from agents.content_agent import service

router = APIRouter()

@router.get("/")
async def content_root():
    return {"agent": "Content Agent", "status": "active"}

@router.post("/generate")
async def generate_lessons(syllabus: str = Form(...)):
    """
    Generates lessons and topics from plain text syllabus input.
    """
    data = service.generate_content(syllabus)
    return {"status": "success", "data": data}

@router.post("/upload")
async def upload_syllabus(file: UploadFile = File(...)):
    """
    Uploads a syllabus file (.pdf, .docx, .csv) and extracts its contents.
    """
    try:
        text = service.upload_and_parse(file)
        data = service.generate_content(text)
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
