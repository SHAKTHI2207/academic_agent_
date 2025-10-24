from fastapi import FastAPI

# Initialize FastAPI
app = FastAPI(
    title="Brok AI Academic Agent (Core)",
    description="Minimal working API version for testing deployment",
    version="0.1"
)

# ✅ Temporary root route
@app.get("/")
async def root():
    return {"message": "Brok AI server is running fine 🚀"}

# ✅ Temporary test endpoint
@app.post("/workflow/run_async")
async def run_workflow_async(syllabus: str):
    return {
        "status": "success",
        "workflow_result": {
            "workflow_name": "Minimal Academic Workflow",
            "syllabus_received": syllabus,
            "execution": "mock-test-success"
        }
    }
