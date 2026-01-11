# Astra AI — Developer Guide

This guide is designed to help developers understand how to work with Astra AI’s codebase, contribute effectively, and extend the system safely.  
It complements the architecture, safety, and roadmap documents by providing hands‑on guidance for building and modifying Astra AI.

---

## 1. Getting Started

### **1.1 Prerequisites**
- Python 3.9 or later  
- Basic familiarity with virtual environments  
- An LLM backend (local or API‑based)  
- Git for version control  

### **1.2 Setting Up the Project**
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/astra-ai.git
cd astra-ai
pip install -r requirements.txt
```

### **1.3 Running Astra AI (Development Mode)**

```bash
python src/interface/cli.py
```

This launches the command‑line interface using the default backend and configuration.

---

## 2. Codebase Overview

Astra AI is organized into clear, modular components:

```
src/
│
├── core/        # Engine, routing, config
├── safety/      # Filters, refusal logic, safety policies
├── interface/   # CLI, API, utilities
└── models/      # Backend adapters
```

Each module has a single responsibility and can be extended independently.

---

## 3. Development Workflow

### **3.1 Branching Model**
Use feature branches:

```
feature/my-new-feature
bugfix/fix-safety-check
docs/update-architecture
```

Avoid committing directly to `main`.

### **3.2 Making Changes**
Before writing code:
- Check open issues  
- Open a new issue if needed  
- Discuss major changes with maintainers  

### **3.3 Submitting Pull Requests**
A good PR includes:
- A clear description of the change  
- References to related issues  
- Tests (if applicable)  
- Documentation updates (if needed)  

---

## 4. Working With the Core Engine

The core engine handles:
- request routing  
- prompt assembly  
- conversation state  
- backend communication  

Key files:
- `engine.py` — main processing loop  
- `router.py` — directs requests to modules  
- `config.py` — environment and backend settings  

When modifying the engine:
- keep logic modular  
- avoid embedding safety checks here  
- ensure new features don’t bypass the safety layer  

---

## 5. Working With the Safety Layer

Safety is central to Astra AI’s design.

### **5.1 Filters**
Located in `src/safety/filters.py`, these detect:
- harmful intent  
- unsafe content  
- jailbreak attempts  

Filters should be:
- transparent  
- easy to audit  
- deterministic  

### **5.2 Refusal Logic**
Located in `src/safety/refusal_logic.py`, this module:
- generates consistent refusals  
- maintains tone and clarity  
- avoids revealing internal logic  

When adding new refusal patterns:
- keep them short  
- avoid moralizing  
- maintain a professional tone  

---

## 6. Working With Prompts

Prompts live in the `prompts/` directory.

### **6.1 System Prompt**
`system_prompt.md` defines:
- identity  
- tone  
- safety rules  
- behavioral principles  

Changes to this file should be:
- discussed in an issue  
- versioned  
- tested for regressions  

### **6.2 Prompt Modules**
Future expansions may include:
- domain‑specific prompts  
- personality variants  
- tool‑use instructions  

Keep modules small and focused.

---

## 7. Adding a New Model Backend

Backends live in `src/models/`.

To add a new backend:
1. Create a new adapter file  
2. Implement the standard interface:
   - `generate(prompt)`  
   - `configure(settings)`  
3. Register the backend in `config.py`  

Backends should:
- normalize responses  
- avoid embedding safety logic  
- handle errors gracefully  

---

## 8. Extending the Interface Layer

The interface layer includes:
- CLI (`cli.py`)  
- API (`api.py`)  
- shared utilities (`utils.py`)  

When adding new interfaces:
- keep them thin  
- avoid duplicating logic  
- route all requests through the core engine  

---

## 9. Testing

Tests live in the `tests/` directory.

### **9.1 Types of Tests**
- **Unit tests** for core logic  
- **Safety tests** for refusal behavior  
- **Integration tests** for end‑to‑end flows  

### **9.2 Running Tests**

```bash
pytest
```

### **9.3 Writing New Tests**
Tests should:
- be deterministic  
- avoid calling external APIs  
- cover edge cases  

---

## 10. Logging & Debugging

Astra AI uses lightweight logging for:
- request flow  
- safety decisions  
- backend interactions  

When debugging:
- avoid logging sensitive data  
- keep logs readable  
- use debug mode sparingly  

---

## 11. Style & Conventions

### **11.1 Code Style**
- Follow PEP 8  
- Use descriptive variable names  
- Keep functions small and focused  

### **11.2 Documentation**
- Document public functions  
- Update docs when behavior changes  
- Keep comments concise  

### **11.3 Commit Messages**
Use clear, action‑oriented messages:

```
Add new safety filter for harmful intent
Refactor prompt assembly logic
Fix backend adapter error handling
```

---

## 12. Contributing Safely

All contributions must:
- respect Astra AI’s safety philosophy  
- avoid introducing harmful behavior  
- maintain transparency  
- preserve modularity  

If unsure, open an issue to discuss your idea.

---

## 13. Getting Help

If you need guidance:
- open an issue  
- join discussions  
- ask maintainers for clarification  

Astra AI thrives on collaboration.

---

## 14. Versioning

**Developer Guide Version:** 1.0  
**Last Updated:** _January 10, 2026_
