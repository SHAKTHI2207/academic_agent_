"""
api/main.py
Brok AI Academic API - Modular Multi-Agent FastAPI Interface
------------------------------------------------------------
Connects all agents + orchestrator via routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.middleware.logging import RequestLogger
app.add_middleware(RequestLogger)

# Import Routers
from agents.content_agent.routes import router as content_router
from agents.exam_agent.routes import router as exam_router
from agents.rubric_agent.routes import router as rubric_router
from agents.evaluator_agent.routes import router as evaluator_router
from agents.analytics_agent.routes import router as analytics_router
from core.workflow_async import run_workflow_async

app = FastAPI(
    title="Brok Academic AI API",
    version="3.0",
    description="Autonomous academic orchestration system powered by Brok AI"
)

# Enable CORS for front-end or local dashboard integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(content_router, prefix="/content", tags=["Content Agent"])
app.include_router(exam_router, prefix="/exam", tags=["Exam Agent"])
app.include_router(rubric_router, prefix="/rubric", tags=["Rubric Agent"])
app.include_router(evaluator_router, prefix="/evaluate", tags=["Evaluator Agent"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics Agent"])

# Workflow Execution Endpoint
@app.post("/workflow/run_async")
async def execute_full_workflow(syllabus: str):
    """Triggers full Brok AI academic workflow."""
    return await run_workflow_async(syllabus)
