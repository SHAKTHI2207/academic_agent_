"""
agents/exam_agent/service.py
----------------------------
Exam Agent: Generates questions, quizzes, and viva prompts from syllabus.
"""

from datetime import datetime

class ExamAgent:
    def __init__(self):
        self.role = "Assessment Designer"
        self.goal = "Create fair and diverse academic evaluations."
        self.version = "v1.0"

    def generate_exam(self, syllabus_text: str):
        """
        Generates exam questions from syllabus topics.
        """
        topics = [t.strip() for t in syllabus_text.split(",") if t.strip()]
        questions = [
            {"question": f"Explain the core concepts of {topic}.", "marks": 10}
            for topic in topics
        ]
        result = {
            "agent": "ExamAgent",
            "generated_on": datetime.utcnow().isoformat(),
            "questions": questions,
            "total_questions": len(questions)
        }
        return result

# Global instance
agent = ExamAgent()

def generate_exam(syllabus_text: str):
    return agent.generate_exam(syllabus_text)
