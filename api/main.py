from fastapi import FastAPI
from agents.content_agent.routes import router as content_router
from agents.exam_agent.routes import router as exam_router
from agents.rubric_agent.routes import router as rubric_router
from agents.evaluator_agent.routes import router as evaluator_router
from agents.analytics_agent.routes import router as analytics_router

app = FastAPI(title="Academic Agent Core", version="0.1.0")

app.include_router(content_router, prefix="/content", tags=["Content Agent"])
app.include_router(exam_router, prefix="/exam", tags=["Exam Agent"])
app.include_router(rubric_router, prefix="/rubric", tags=["Rubric Agent"])
app.include_router(evaluator_router, prefix="/evaluate", tags=["Evaluator Agent"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics Agent"])

@app.get("/")
def root():
    return {"message": "Academic Agent Core API Running"}
