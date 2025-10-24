"""
agents/analytics_agent/routes.py
--------------------------------
Routes for Analytics Agent — handles performance insights and analytics.
"""

from fastapi import APIRouter, Form
from agents.analytics_agent import service

router = APIRouter()

@router.get("/")
async def analytics_root():
    return {"agent": "Analytics Agent", "status": "active"}

@router.post("/analyze")
async def analyze_data(syllabus: str = Form(...)):
    """
    Generates visual and textual analytics based on student or syllabus data.
    """
    data = service.analyze_performance(syllabus)
    return {"status": "success", "data": data}
