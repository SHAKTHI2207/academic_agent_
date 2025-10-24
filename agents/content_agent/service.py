"""
agents/content_agent/service.py
-------------------------------
Content Agent: Handles academic content generation and syllabus extraction.
Supports file uploads (.pdf, .docx, .csv) and text-based inputs.
"""

import os
from datetime import datetime
import csv
import docx
import PyPDF2

UPLOAD_DIR = "data/uploads/content_agent"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class ContentAgent:
    def __init__(self):
        self.role = "Academic Author"
        self.goal = "Generate structured lessons, summaries, and diagrams."
        self.version = "v1.0"

    # -------------------------
    # 🔹 File Handling
    # -------------------------
    def handle_file_upload(self, file):
        """
        Saves the uploaded file locally and extracts text based on file type.
        """
        filename = file.filename
        filepath = os.path.join(UPLOAD_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(file.file.read())

        ext = filename.split(".")[-1].lower()
        if ext == "pdf":
            text = self.extract_text_from_pdf(filepath)
        elif ext == "docx":
            text = self.extract_text_from_docx(filepath)
        elif ext == "csv":
            text = self.extract_text_from_csv(filepath)
        else:
            raise ValueError("Unsupported file type.")
        return text

    def extract_text_from_pdf(self, filepath):
        text = ""
        with open(filepath, "rb") as pdf:
            reader = PyPDF2.PdfReader(pdf)
            for page in reader.pages:
                text += page.extract_text()
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
    # 🔹 Content Generation
    # -------------------------
    def generate_content(self, syllabus_text: str):
        """
        Converts raw syllabus text into structured lessons and topics.
        """
        topics = self.extract_topics(syllabus_text)
        lessons = [
            {"topic": t, "summary": f"Generated notes for {t}", "created_at": datetime.utcnow().isoformat()}
            for t in topics
        ]
        result = {
            "agent": "ContentAgent",
            "generated_on": datetime.utcnow().isoformat(),
            "topics": topics,
            "lessons": lessons,
        }
        return result

    def extract_topics(self, text: str):
        """
        Simple mock — extracts Title-case words as topics.
        """
        words = text.split()
        topics = list({word for word in words if word.istitle() and len(word) > 3})
        return topics or ["Introduction", "Fundamentals", "Applications"]


# Instantiate global agent
agent = ContentAgent()

def generate_content(syllabus_text: str):
    return agent.generate_content(syllabus_text)

def upload_and_parse(file):
    return agent.handle_file_upload(file)
