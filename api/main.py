"""
api/main.py
------------
Asynchronous multi-agent orchestration for Brok AI Academic Agent System.
"""

# ==========================================================
# ✅ IMPORTS
# ==========================================================
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
import sys, os, asyncio
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
# ✅ FASTAPI APP INIT
# ==========================================================
app = FastAPI(
    title="Brok AI Academic Agent System",
    description="Asynchronous AI-based academic automation framework with multi-agent architecture.",
    version="3.0"
)

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
# ✅ ROOT & HEALTH ENDPOINTS
# ==========================================================
@app.get("/")
async def root():
    return {
        "message": "Welcome to Brok AI Academic Agent API 🚀",
        "version": "3.0",
        "architecture": "Asynchronous Agent Orchestration",
        "agents": [
            "Content", "Exam", "Rubric", "Evaluator", "Analytics"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "ok", "uptime": "active", "mode": "async", "version": "3.0"}

# ==========================================================
# ✅ ASYNC AGENT ORCHESTRATION
# ==========================================================
async def run_content_agent(syllabus):
    from agents.content_agent import service
    return {"Content Agent": service.generate_content(syllabus)}

async def run_exam_agent(syllabus):
    from agents.exam_agent import service
    return {"Exam Agent": service.generate_exam(syllabus)}

async def run_rubric_agent(syllabus):
    from agents.rubric_agent import service
    return {"Rubric Agent": service.design_rubric(syllabus)}

async def run_evaluator_agent(syllabus):
    from agents.evaluator_agent import service
    return {"Evaluator Agent": service.evaluate_responses(syllabus)}

async def run_analytics_agent(syllabus):
    from agents.analytics_agent import service
    return {"Analytics Agent": service.analyze_performance(syllabus)}

# ==========================================================
# ✅ MAIN WORKFLOW ENDPOINT
# ==========================================================
@app.post("/workflow/run_async")
async def run_workflow_async(syllabus: str):
    """
    Run all 5 agents asynchronously in parallel.
    Returns combined results once all agents finish.
    """
    try:
        # Run all agents in parallel
        results = await asyncio.gather(
            run_content_agent(syllabus),
            run_exam_agent(syllabus),
            run_rubric_agent(syllabus),
            run_evaluator_agent(syllabus),
            run_analytics_agent(syllabus)
        )

        # Merge results
        merged_output = {}
        for r in results:
            merged_output.update(r)

        return {
            "status": "success",
            "syllabus": syllabus,
            "architecture": "Async Parallel Agent Execution",
            "workflow_results": merged_output
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

# ==========================================================
# ✅ RUN LOCALLY
# ==========================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
