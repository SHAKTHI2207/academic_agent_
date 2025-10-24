"""
agents/content_agent/service.py
-------------------------------
Implements backend logic for Content Agent.
"""

import io

def generate_content(syllabus: str):
    """
    Generates content (mock logic for now).
    You can replace this later with GPT-based summarization or QnA generation.
    """
    lessons = [f"Lesson {i+1}: {topic.strip().capitalize()}" for i, topic in enumerate(syllabus.split(','))]
    return {"generated_lessons": lessons, "total_lessons": len(lessons)}

def upload_and_parse(file):
    """
    Parses uploaded file (.pdf, .docx, .csv) — simplified placeholder.
    """
    filename = file.filename.lower()
    contents = file.file.read().decode("utf-8", errors="ignore")

    # For now, just return text (pretend we parsed it)
    return contents[:500]  # return first 500 chars as preview
