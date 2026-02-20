# Astra AI

## Overview
Astra AI is a multipurpose, open-source conversational AI built for clarity, trust, and transparency. It provides a CLI-based chat interface with built-in safety filters and jailbreak resistance.

## Project Architecture
- **src/core/**: Core processing logic (engine.py, router.py, config.py)
- **src/safety/**: Safety guardrails (filters.py, refusal_logic.py)
- **src/interface/**: User-facing components (cli.py, api.py, utils.py)
- **src/models/**: Backend adapters for LLM integration (backend_adapter.py)
- **prompts/**: System prompt definition (system_prompt.md)
- **run_astra.py**: Main entry point

## How to Run
```bash
python run_astra.py
```

## Current State
- CLI interface is functional with template-based responses
- Safety filters and refusal logic are implemented
- Backend adapter uses a local template system (no external LLM connected)
- API module is a placeholder for future REST API implementation

## Technical Details
- **Language**: Python 3.12
- **No external dependencies** required for basic operation
- **Configuration**: Environment variables via src/core/config.py
  - ASTRA_MODEL_BACKEND: Backend type (default: "local")
  - ASTRA_MODEL_NAME: Model name
  - ASTRA_API_KEY: API key for external backends
  - ASTRA_SYSTEM_PROMPT_PATH: Path to system prompt file
