"""
agents/exam_agent/service.py
----------------------------
Exam Agent — Smart assessment generator with self-awareness layer.
Supports .csv, .docx uploads for question banks and prevents hallucination duplication.
"""

import os
import csv
import docx
import random
import hashlib
from datetime import datetime
from difflib import SequenceMatcher

UPLOAD_DIR = "data/uploads/exam_agent"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class ExamAgent:
    def __init__(self):
        self.role = "Assessment Designer"
        self.goal = "Create diverse, non-repetitive question sets with self-awareness."
        self.version = "v2.0"
        self.generated_questions = []  # memory cache for hallucination detection

    # -------------------------
    # 🔹 File Handling
    # -------------------------
    def handle_file_upload(self, file):
        filename = file.filename
        filepath = os.path.join(UPLOAD_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(file.file.read())

        ext = filename.split(".")[-1].lower()
        if ext == "docx":
            text = self.extract_text_from_docx(filepath)
        elif ext == "csv":
            text = self.extract_text_from_csv(filepath)
        else:
            raise ValueError("Unsupported file type. Please upload .docx or .csv only.")
        return text

    def extract_text_from_docx(self, filepath):
        text = ""
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    def extract_text_from_csv(self, filepath):
        text = ""
        with open(filepath, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                text += " ".join(row) + "\n"
        return text

    # -------------------------
    # 🔹 Smart Question Generation
    # -------------------------
    def generate_questions(self, topics, num_questions=5):
        """
        Generates unique, context-aware questions from topics.
        Includes self-awareness layer for hallucination detection.
        """
        generated = []
        for t in topics:
            for i in range(num_questions):
                q_text = self.create_unique_question(t)
                if not self.is_hallucinated(q_text):
                    generated.append({
                        "topic": t,
                        "question": q_text,
                        "type": random.choice(["MCQ", "Short Answer", "Viva"]),
                        "difficulty": random.choice(["easy", "medium", "hard"]),
                        "created_at": datetime.utcnow().isoformat()
                    })
                    self.generated_questions.append(q_text)

        return {
            "agent": "ExamAgent",
            "generated_on": datetime.utcnow().isoformat(),
            "questions": generated
        }

    # -------------------------
    # 🧠 Self-Awareness Layer
    # -------------------------
    def create_unique_question(self, topic):
        """Simple random variation in question phrasing."""
        formats = [
            f"Explain the core principles of {topic}.",
            f"What are real-world applications of {topic}?",
            f"Define {topic} and discuss its importance in AI systems.",
            f"How does {topic} impact computational design?",
            f"List the advantages and challenges of {topic}."
        ]
        return random.choice(formats)

    def is_hallucinated(self, new_question, threshold=0.85):
        """
        Detects hallucinations / duplicates using fuzzy string matching.
        """
        for existing in self.generated_questions:
            sim = SequenceMatcher(None, new_question.lower(), existing.lower()).ratio()
            if sim > threshold:
                print(f"⚠️ Self-Awareness: Similar question detected → '{new_question}' ~ '{existing}'")
                return True
        return False


# Global instance
agent = ExamAgent()

def create_assessments(content_data):
    topics = content_data.get("topics", [])
    return agent.generate_questions(topics)

def upload_and_parse(file):
    return agent.handle_file_upload(file)
