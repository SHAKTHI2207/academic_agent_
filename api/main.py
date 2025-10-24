# ==========================================================
# 🚀 Brok AI Academic Agent - FastAPI Main Entry (Stable Build)
# ==========================================================

# --- PATH FIX FOR COLAB + PYTHON IMPORTS ---
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# --- FASTAPI CORE IMPORTS ---
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- CUSTOM MIDDLEWARE (SAFE IMPORT) ---
try:
    from api.middleware.logging import RequestLogger
except ModuleNotFoundError:
    RequestLogger = None  # Skip if not available

# --- IMPORT AGENT ROUTERS ---
from agents.content_agent.routes import router as content_router
from agents.exam_agent.routes import router as exam_router
from agents.rubric_agent.routes import router as rubric_router
from agents.evaluator_agent.routes import router as evaluator_router
from agents.analytics_agent.routes import router as analytics_router

# --- INITIALIZE FASTAPI APP ---
app = FastAPI(
    title="Brok AI Academic Agent System",
    description="Autonomous academic workflow automation system with 5 intelligent agents",
    version="1.0.0"
)

# --- MIDDLEWARE SETUP ---
if RequestLogger:
    app.add_middleware(RequestLogger)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins during testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ROUTER REGISTRATION ---
app.include_router(content_router, prefix="/content", tags=["Content Agent"])
app.include_router(exam_router, prefix="/exam", tags=["Exam Agent"])
app.include_router(rubric_router, prefix="/rubric", tags=["Rubric Agent"])
app.include_router(evaluator_router, prefix="/evaluate", tags=["Evaluator Agent"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics Agent"])

# --- ROOT ENDPOINT ---
@app.get("/")
async def root():
    return {
        "message": "Welcome to Brok AI Academic Agent API 🚀",
        "status": "Server Running",
        "active_agents": [
            "Content Agent", "Exam Agent", "Rubric Agent",
            "Evaluator Agent", "Analytics Agent"
        ]
    }

# --- WORKFLOW ORCHESTRATION ENDPOINT ---
@app.post("/workflow/run_async")
async def run_workflow_async(syllabus: str):
    """
    Triggers the asynchronous academic workflow simulation.
    In production, this will coordinate multi-agent async orchestration.
    """
    return {
        "status": "success",
        "workflow_result": {
            "workflow_name": "Async Academic Agent Architecture",
            "syllabus_received": syllabus,
            "execution_mode": "simulated (v1.0.0)"
        }
    }

# --- HEALTH CHECK ENDPOINT ---
@app.get("/health")
async def health():
    return {"status": "ok", "uptime": "active", "service": "Brok AI Academic API"}
