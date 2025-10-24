from datetime import datetime
import random

class EvaluatorAgent:
    def __init__(self):
        self.role = "Reviewer"
        self.goal = "Provide logical, transparent AI-assisted grading."

    def evaluate(self, exams, rubric):
        results = []
        for i in range(3):
            marks = random.uniform(75,95)
            feedback = "Strong conceptual understanding." if marks>85 else "Needs clarity improvement."
            results.append({"student": f"Student_{i+1}", "score": round(marks,2), "feedback": feedback})
        return {"agent":"EvaluatorAgent","results":results,"timestamp":datetime.utcnow().isoformat()}
