from datetime import datetime
import random

class RubricAgent:
    def __init__(self):
        self.role = "Evaluation Architect"
        self.goal = "Build fair and balanced rubric matrices."
        self.memory = []

    def create_rubric(self, exams):
        rubric = {"criteria": {}, "levels": ["Poor","Good","Excellent"]}
        for q in exams.get("questions", []):
            topic = q["topic"]
            if topic not in rubric["criteria"]:
                rubric["criteria"][topic] = {
                    "knowledge": random.uniform(0.3,0.5),
                    "clarity": random.uniform(0.2,0.4),
                    "creativity": random.uniform(0.1,0.3)
                }
        self.memory.append(rubric)
        return {"agent":"RubricAgent","rubric":rubric,"timestamp":datetime.utcnow().isoformat()}
