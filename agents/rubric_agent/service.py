"""
agents/rubric_agent/service.py
------------------------------
Rubric Agent: Designs evaluation rubrics for objective grading.
"""

from datetime import datetime

class RubricAgent:
    def __init__(self):
        self.role = "Rubric Architect"
        self.goal = "Define fair and transparent evaluation criteria."
        self.version = "v1.0"

    def design_rubric(self, syllabus_text: str):
        criteria = ["Knowledge", "Clarity", "Creativity", "Application"]
        rubric = {
            c: f"Evaluate {c.lower()} level for each student submission." for c in criteria
        }
        return {
            "agent": "RubricAgent",
            "generated_on": datetime.utcnow().isoformat(),
            "criteria": rubric,
            "syllabus": syllabus_text
        }

# Global instance
agent = RubricAgent()

def design_rubric(syllabus_text: str):
    return agent.design_rubric(syllabus_text)
