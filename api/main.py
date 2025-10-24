from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.request_logger import RequestLogger

# Import all agent routers
from agents.content_agent.routes import router as content_router
from agents.exam_agent.routes import router as exam_router
from agents.rubric_agent.routes import router as rubric_router
from agents.evaluator_agent.routes import router as evaluator_router
from agents.analytics_agent.routes import router as analytics_router

# Initialize FastAPI app
app = FastAPI(
    title="Brok AI Academic Agent System",
    description="Autonomous academic workflow automation framework with modular agents",
    version="1.0.0"
)

# Apply Middleware
app.add_middleware(RequestLogger)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Register Routers
app.include_router(content_router, prefix="/content", tags=["Content Agent"])
app.include_router(exam_router, prefix="/exam", tags=["Exam Agent"])
app.include_router(rubric_router, prefix="/rubric", tags=["Rubric Agent"])
app.include_router(evaluator_router, prefix="/evaluate", tags=["Evaluator Agent"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics Agent"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Brok AI Academic Agent API 🚀"}

# Workflow orchestration endpoint
@app.post("/workflow/run_async")
async def run_workflow_async(syllabus: str):
    """
    This endpoint triggers the asynchronous academic agent workflow.
    For now, it returns a mock response for testing.
    """
    return {
        "status": "success",
        "workflow_result": {
            "workflow_name": "Async Academic Agent Architecture",
            "syllabus_received": syllabus,
            "execution": "simulated"
        }
    }
