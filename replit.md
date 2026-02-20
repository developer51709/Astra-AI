# Astra AI

## Overview
Astra AI is a multipurpose, open-source conversational AI built for clarity, trust, and transparency. It provides a CLI-based chat interface with built-in safety filters and jailbreak resistance, powered by OpenAI via Replit AI Integrations.

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
- CLI interface is functional with real AI responses via OpenAI (gpt-5)
- Safety filters and refusal logic are implemented
- Backend adapter uses Replit AI Integrations for OpenAI access
- API module is a placeholder for future REST API implementation

## Technical Details
- **Language**: Python 3.11
- **Dependencies**: openai, colorama (managed via requirements.txt)
- **AI Backend**: OpenAI gpt-5 via Replit AI Integrations (no personal API key needed)
- **Configuration**: Environment variables via src/core/config.py
  - AI_INTEGRATIONS_OPENAI_API_KEY: Auto-set by Replit AI Integrations
  - AI_INTEGRATIONS_OPENAI_BASE_URL: Auto-set by Replit AI Integrations
  - ASTRA_SYSTEM_PROMPT_PATH: Path to system prompt file (default: prompts/system_prompt.md)
