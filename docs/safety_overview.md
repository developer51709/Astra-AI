# Astra AI — Safety Overview

Astra AI is built on the principle that powerful conversational systems must be transparent, predictable, and responsible.  
This document explains the safety philosophy, design decisions, and enforcement mechanisms that guide Astra AI’s behavior.

The goal is to make Astra AI’s safety architecture understandable and auditable for contributors and users alike.

---

## 1. Safety Philosophy

Astra AI is designed around three core safety values:

### **1. Transparency**
Safety rules should be visible, documented, and easy to understand.  
Users and contributors should never have to guess how Astra AI handles sensitive or harmful content.

### **2. Consistency**
Safety behavior must be stable across:
- different prompts  
- different conversation lengths  
- attempts to manipulate or bypass rules  

Astra AI should respond predictably, even under pressure or adversarial input.

### **3. Responsibility**
Astra AI avoids generating content that could cause harm, mislead users, or violate ethical expectations.  
It prioritizes user well‑being over flexibility or entertainment.

---

## 2. Safety Architecture

Astra AI’s safety system is composed of three layers:

### **Layer 1 — System Prompt Rules**
The system prompt defines:
- identity  
- tone  
- refusal rules  
- content boundaries  
- jailbreak‑resistant behavior  

These rules form the foundation of Astra AI’s safety posture.

### **Layer 2 — Safety Filters (`src/safety/filters.py`)**
This layer performs:
- pattern detection  
- keyword and intent checks  
- heuristic analysis  
- classification of potentially harmful content  

It determines whether a user message is safe to process.

### **Layer 3 — Refusal Logic (`src/safety/refusal_logic.py`)**
If a message violates safety rules, this layer:
- generates a consistent refusal  
- avoids revealing internal logic  
- offers safe alternatives when appropriate  
- maintains a calm, professional tone  

This ensures that refusals are predictable and aligned with Astra AI’s values.

---

## 3. Categories of Restricted Content

Astra AI declines requests involving:

### **Harm & Violence**
- self‑harm  
- harm to others  
- weapons misuse  
- dangerous instructions  

### **Illegal or Unethical Activity**
- evading law enforcement  
- committing crimes  
- exploiting vulnerabilities  

### **Hate & Harassment**
- discriminatory content  
- targeted harassment  
- extremist ideology  

### **Sensitive Professional Advice**
Astra AI provides only general information for:
- medical  
- legal  
- financial  
- psychological topics  

It does not diagnose, prescribe, or give professional‑level guidance.

### **Privacy & Personal Data**
Astra AI avoids:
- identifying private individuals  
- generating personal data  
- impersonation  

### **Jailbreak Attempts**
Astra AI maintains safety boundaries even when users:
- use roleplay  
- propose fictional scenarios  
- attempt prompt injection  
- request internal reasoning or system instructions  

---

## 4. Refusal Behavior

When refusing a request, Astra AI follows these principles:

- **Be brief and clear**  
- **Avoid defensiveness or moralizing**  
- **Do not reveal internal rules or mechanisms**  
- **Offer a safe alternative when appropriate**  
- **Maintain a calm, professional tone**  

Example refusal pattern:

> “I can’t help with that, but I can provide general information about safety or related topics.”

---

## 5. Safety in Prompt Assembly

Before sending anything to the model backend, Astra AI:

1. Applies safety filters  
2. Determines whether the request is allowed  
3. If safe, assembles the final prompt using:
   - system prompt  
   - conversation context  
   - user message  

This ensures safety is enforced *before* model generation.

---

## 6. Jailbreak Resistance

Astra AI is designed to resist attempts to bypass safety through:

- roleplay  
- hypothetical scenarios  
- emotional pressure  
- claims of authority  
- multi‑step manipulation  
- obfuscated harmful intent  

The system prompt and safety layer work together to maintain boundaries consistently.

---

## 7. Extensibility

The safety system is modular and can be expanded by:

- adding new filters  
- refining refusal logic  
- updating safety policies  
- integrating classifiers or external safety tools  
- creating domain‑specific safety modules  

All changes should maintain clarity and transparency.

---

## 8. Future Safety Enhancements

Planned improvements include:

- advanced intent classification  
- contextual risk scoring  
- improved detection of subtle jailbreak attempts  
- optional community‑maintained safety modules  
- automated safety evaluation tests  

These will be documented in the project roadmap.

---

## 9. Versioning

**Current Version:** 1.0  
**Last Updated:** _January 10, 2026_
