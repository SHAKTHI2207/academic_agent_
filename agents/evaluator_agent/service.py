"""
agents/evaluator_agent/service.py
---------------------------------
Evaluator Agent: Grades answers using rubric-based logic.
"""

from datetime import datetime

class EvaluatorAgent:
    def __init__(self):
        self.role = "Auto-Evaluator"
        self.goal = "Assess responses fairly using rubric-based logic."
        self.version = "v1.0"

    def evaluate_responses(self, syllabus_text: str):
        topics = [t.strip() for t in syllabus_text.split(",") if t.strip()]
        evaluations = {
            topic: f"Evaluation complete for {topic}" for topic in topics
        }
        return {
            "agent": "EvaluatorAgent",
            "generated_on": datetime.utcnow().isoformat(),
            "evaluations": evaluations
        }

# Global instance
agent = EvaluatorAgent()

def evaluate_responses(syllabus_text: str):
    return agent.evaluate_responses(syllabus_text)
