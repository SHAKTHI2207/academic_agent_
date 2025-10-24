# Academic Agent Core

This repository defines the modular architecture for an AI-driven Academic Automation System inspired by Brok AI principles.
Each agent operates as a distinct service to handle content generation, assessment, rubric creation, evaluation, and analytics.

## Agent Modules
1. Content Agent — Generates lessons, summaries, diagrams.
2. Exam Agent — Creates quizzes, viva, and assignments.
3. Rubric Agent — Builds rubrics and evaluation criteria.
4. Evaluator Agent — Scores student submissions using rubric.
5. Analytics Agent — Generates insights, charts, and reports.

## Quick Start
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## License
© 2025 Shakthivel M under Brok AI — All rights reserved.
