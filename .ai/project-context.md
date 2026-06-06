# AI Project Context & Guidelines

This document provides system-level context for AI tools (such as Cursor, Windsurf, Copilot, or Antigravity) working on this repository.

## 🎯 Repository Goal
This repository tracks the transition of a **Web & Frontend Software Engineer** into an **AI Engineer**. The roadmap is structured over **24 weeks**, split into 5 thematic phases.

## 📁 Directory Structure Rules
- The code is organized into 5 phase folders:
  - `phase-1-python-foundations/`
  - `phase-2-machine-learning-core/`
  - `phase-3-deep-learning-nlp/`
  - `phase-4-ai-engineering/`
  - `phase-5-portfolio-career/`
- Inside each phase, folders are split into **individual weeks** (`week-01`, `week-02`, etc.).
- Inside each week folder, topics are modularly split into **concept subdirectories** (e.g. `01-python-syntax-oop/`), and a `projects/` directory containing weekly projects.
- **Rule:** Every directory (phase, week, concept, project) must contain a `README.md` file to document instructions, logs, and notes.

## 🐍 Python Virtual Environment Rule
- **Optimal Setup:** To save disk space and simplify IDE interpreter settings, use a **single Python virtual environment (`.venv`) initialized at the root of the workspace**.
- Do NOT create separate virtual environments in individual week or project directories.
- Add `.venv` to the root `.gitignore`.

## 💻 Coding & Stack Standards
- **AI Stack:** PyTorch, Hugging Face, LangChain, Pinecone, FastAPI.
- **Frontend Stack:** HTML, Javascript, Next.js, CSS.
- **Integration Principle:** Whenever building an AI backend or model, think about how to interface it with a beautiful web frontend to showcase full-stack AI capabilities.
- **Comments/Documentation:** Preserve existing code comments. Write clear, type-hinted Python code using docstrings where appropriate.

## 🤖 Assistant Behavior
When helping the user write code or explore files:
1. Ensure files are written in their correct week or concept subdirectory.
2. Structure python files cleanly, separating data processing, model logic, and API route definitions.
3. Reference the progress tracker in `.ai/progress-tracker.md` to see what is currently in progress.
