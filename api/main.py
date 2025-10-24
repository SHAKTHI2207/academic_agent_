"""
api/main.py
------------
Main entry point for the Brok AI Academic Agent API.
Handles routing, middleware, and workflow orchestration.
"""

# ==========================================================
# ✅ IMPORTS
# ==========================================================
import sys, os, asyncio, httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- Fix path for Colab ---
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

# ==========================================================
# ✅ ROUTER IMPORTS
# ==========================================================
from agents.content_agent.routes import router as content_router
from agents.exam_agent.routes import router as exam_router
from agents.rubric_agent.routes import router as rubric_router
from agents.evaluator_agent.routes import router as evaluator_router
from agents.analytics_agent.routes import router as analytics_router

# ==========================================================
# ✅ APP INITIALIZATION
# ==========================================================
app = FastAPI(
    title="Brok AI Academic Agent System",
    description="A modular AI-based academic automation framework with multi-agent architecture.",
    version="2.0"
)

# Allow all origins (for testing on Colab)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers
app.include_router(content_router, prefix="/content", tags=["Content Agent"])
app.include_router(exam_router, prefix="/exam", tags=["Exam Agent"])
app.include_router(rubric_router, prefix="/rubric", tags=["Rubric Agent"])
app.include_router(evaluator_router, prefix="/evaluate", tags=["Evaluator Agent"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics Agent"])

# ==========================================================
# ✅ ROOT & HEALTH ROUTES
# ==========================================================
@app.get("/")
async def root():
    return {
        "message": "Welcome to Brok AI Academic Agent API 🚀",
        "status": "running",
        "agents": [
            "Content", "Exam", "Rubric", "Evaluator", "Analytics"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "ok", "uptime": "active", "version": "2.0"}

# ==========================================================
# ✅ WORKFLOW ORCHESTRATOR
# ==========================================================
@app.post("/workflow/run_async")
async def run_workflow_async(syllabus: str):
    """
    Simulates a multi-agent academic workflow asynchronously.
    Each agent is called sequentially via internal logic.
    """
    # 1️⃣ Local agent calls (simulate API chaining)
    from agents.content_agent import service as content
    from agents.exam_agent import service as exam
    from agents.rubric_agent import service as rubric
    from agents.evaluator_agent import service as evaluator
    from agents.analytics_agent import service as analytics

    try:
        content_data = content.generate_content(syllabus)
        exam_data = exam.generate_exam(syllabus)
        rubric_data = rubric.design_rubric(syllabus)
        evaluation_data = evaluator.evaluate_responses(syllabus)
        analytics_data = analytics.analyze_performance(syllabus)

        result = {
            "Content Agent": content_data,
            "Exam Agent": exam_data,
            "Rubric Agent": rubric_data,
            "Evaluator Agent": evaluation_data,
            "Analytics Agent": analytics_data
        }

        return {"status": "success", "workflow": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# ==========================================================
# ✅ APP ENTRY POINT (LOCAL MODE)
# ==========================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
