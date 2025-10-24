"""
core/workflow.py
----------------
Synchronous Academic Agent Workflow (Debug / Readable Mode)
-----------------------------------------------------------
Executes the full academic architecture step-by-step, sequentially.
Useful for testing, debugging, or non-async environments.
"""

from datetime import datetime

# Import all agents
from agents.content_agent import service as content_agent
from agents.exam_agent import service as exam_agent
from agents.rubric_agent import service as rubric_agent
from agents.evaluator_agent import service as evaluator_agent
from agents.analytics_agent import service as analytics_agent


def run_workflow(syllabus_text: str):
    """
    Executes the full academic AI workflow in synchronous mode.
    Returns a structured JSON log of all stages and outputs.
    """
    print("\n============================")
    print("🧠 Starting Academic Workflow (Sync Mode)")
    print("============================")

    logs = {"stages": [], "timestamp": datetime.utcnow().isoformat()}

    # Stage 1 → Content Generation
    print("\n🚀 [Stage 1] Content Agent: Generating lessons...")
    content_output = content_agent.generate_content(syllabus_text)
    logs["stages"].append({
        "stage": "content_generation",
        "agent": "ContentAgent",
        "output": content_output,
        "timestamp": datetime.utcnow().isoformat()
    })

    # Stage 2 → Exam Creation
    print("\n🧩 [Stage 2] Exam Agent: Creating assessments...")
    exam_output = exam_agent.create_assessments(content_output)
    logs["stages"].append({
        "stage": "exam_creation",
        "agent": "ExamAgent",
        "output": exam_output,
        "timestamp": datetime.utcnow().isoformat()
    })

    # Stage 3 → Rubric Design
    print("\n⚖️ [Stage 3] Rubric Agent: Designing evaluation matrices...")
    rubric_output = rubric_agent.agent.create_rubric(exam_output)
    logs["stages"].append({
        "stage": "rubric_design",
        "agent": "RubricAgent",
        "output": rubric_output,
        "timestamp": datetime.utcnow().isoformat()
    })

    # Stage 4 → Evaluation
    print("\n📘 [Stage 4] Evaluator Agent: Scoring responses...")
    evaluation_output = evaluator_agent.agent.evaluate(exam_output, rubric_output)
    logs["stages"].append({
        "stage": "evaluation",
        "agent": "EvaluatorAgent",
        "output": evaluation_output,
        "timestamp": datetime.utcnow().isoformat()
    })

    # Stage 5 → Analytics
    print("\n📊 [Stage 5] Analytics Agent: Generating insights...")
    analytics_output = analytics_agent.agent.generate_report(evaluation_output)
    logs["stages"].append({
        "stage": "analytics",
        "agent": "AnalyticsAgent",
        "output": analytics_output,
        "timestamp": datetime.utcnow().isoformat()
    })

    print("\n✅ Academic Workflow Completed Successfully.\n")

    return {
        "workflow_name": "Academic Agent Architecture (Sync Mode)",
        "execution_summary": f"{len(logs['stages'])} stages executed successfully.",
        "pipeline_log": logs
    }


# 🔧 For local test runs:
if __name__ == "__main__":
    result = run_workflow("Artificial Intelligence and Quantum Machine Learning Systems")
    from pprint import pprint
    pprint(result)
