# Academic Agent Core

Brok AI Academic System v3.0

Autonomous Multi-Agent Academic Automation Framework

“Reimagining the academic workflow through asynchronous AI orchestration.”

⸻
 Abstract

Brok AI Academic System (v3.0) introduces an autonomous multi-agent framework that automates the complete academic workflow — from content generation and assessment design to rubric formulation, evaluation, and analytics.

Built on FastAPI and powered by asynchronous agent collaboration, the system achieves up to 80% workflow reduction for instructors and academic institutions.

Each agent operates with independent reasoning logic, allowing parallelized task execution via Python’s asyncio.gather() — enabling real-time collaboration between AI-driven academic sub-systems.

The framework integrates seamlessly with ChatGPT Enterprise, positioning ChatGPT as the Frontend Brain (contextual reasoning, conversation, orchestration) while Brok AI serves as the Backend Engine (execution, data processing, and automation).
______________________________________________________________________________
 Architecture Overview

The Brok AI framework follows a layered asynchronous design inspired by agentic AI systems and distributed microservice architectures.
                        ┌────────────────────────────┐
                        │  ChatGPT Enterprise Agent  │
                        │  "Frontend Brain"          │
                        │  - Context interpretation   │
                        │  - Orchestration logic      │
                        │  - Dialogue interface       │
                        └──────────┬─────────────────┘
                                   │ REST API Calls
                                   ▼
                ┌─────────────────────────────────────────┐
                │           BROK AI BACKEND               │
                │  (FastAPI + Async Agents Architecture)  │
                │-----------------------------------------│
                │  • Content Agent                        │
                │  • Exam Agent                           │
                │  • Rubric Agent                         │
                │  • Evaluator Agent                      │
                │  • Analytics Agent                      │
                └──────────┬──────────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │  Data & Storage Layer    │
                    │  - AWS / SQL / Local     │
                    │  - Vector Memory Support │
                    └──────────────────────────┘
 Each agent operates autonomously but reports to a central orchestrator via the /workflow/run_async endpoint, ensuring complete synchronization of tasks and real-time results.
_____________________________________________________________________

Core Design Principles
	1.	Asynchronous Multi-Agent Execution
Each agent is an independent microservice communicating via FastAPI routes.
Powered by Python’s asyncio.gather(), the system runs agents in parallel, reducing computation latency by 70–80%.
	2.	Modular Architecture
Agents can be added, modified, or replaced without refactoring the core system.
	3.	Explainability & Transparency
Each agent returns JSON-structured reasoning outputs to maintain full traceability.
	4.	Frontend-Backend Division
ChatGPT Enterprise handles cognitive reasoning and orchestration, while Brok AI executes deterministic logic and data-driven operations.
	5.	Scalability & Integration
Deployable on AWS, Render, or Vercel with Docker; ready for API integration with external LMS or enterprise tools.
_____________________________________________________________________________________

Integration with ChatGPT Enterprise

Brok AI integrates directly with ChatGPT Enterprise Custom GPT Agents via REST API endpoints.

Frontend (ChatGPT Enterprise)
Handles reasoning, planning, and interpretation:
	•	Understands syllabus context
	•	Chooses agent routes dynamically
	•	Aggregates JSON responses into conversational summaries

Backend (Brok AI FastAPI)
Executes backend workflows:
	•	/content/generate — Lesson Generation
	•	/exam/create — Question Paper Creation
	•	/rubric/design — Rubric Formulation
	•	/evaluate/evaluate — Auto Grading
	•	/analytics/analyze — Insights

Example GPT Manifest Snippet

actions:
  - name: Run Academic Workflow
    endpoint: POST /workflow/run_async
    parameters:
      syllabus: string
description: >
  Executes asynchronous academic automation workflow 
  including content, exams, rubrics, and analytics.

ChatGPT Enterprise acts as a cognitive interface, while Brok AI serves as the autonomous execution layer.

⸻

Contributors

Lead Architect: Shakthi
AI Systems Researcher | PGDM Student | Quantum-AI Enthusiast

⸻
 License

This repository is licensed under the MIT License.
© 2025 Brok AI — All rights reserved.

⸻

Citation

If referencing this framework in academic or research contexts:
Shakthi (2025). Brok AI Academic System v3.0: 
Autonomous Asynchronous Multi-Agent Academic Framework. 
GitHub Repository: https://github.com/<your-username>/academic_agent_core
------------------------------------------------


## Quick Start
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## License
© 2025 Shakthivel M under Brok AI — All rights reserved.
