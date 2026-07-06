# Sprint 3 Summary

## Sprint Goal

Transform Techie from a generic chatbot into a technology mentor by introducing a well-defined teaching personality through a system prompt.

---

## Features Implemented

### Prompt Service

- Created `PromptService`
- Loads the system prompt from a dedicated markdown file
- Separates prompt engineering from application logic

---

### System Prompt

Created Techie's teaching identity, including:

- Identity
- Mission
- Teaching Philosophy
- Teaching Style
- Communication Guidelines

---

### LLM Service Improvements

Refactored `LLMService` to:

- Build messages separately
- Generate responses through a dedicated method
- Improve readability
- Prepare for future conversation memory

---

### Project Configuration

Added:

- `pyproject.toml`
- VS Code workspace settings
- Ruff formatting configuration
- Type checking support

---

### Evaluation Framework

Created a structured evaluation process for measuring Techie's teaching quality.

Six evaluation scenarios were completed.

---

## Evaluation Results

| Evaluation                | Result                    |
| ------------------------- | ------------------------- |
| Beginner Explanation      | ✅ Pass                   |
| Guided Learning           | ✅ Pass                   |
| Comparing Concepts        | ⚠️ Pass with Improvements |
| Correcting Misconceptions | ⚠️ Pass with Improvements |
| Honest Uncertainty        | ❌ Needs Improvement      |
| Adapting Explanations     | ✅ Pass                   |

Overall Score:

**159 / 180 (88.3%)**

---

## Sprint Outcome

Sprint 3 successfully transformed Techie into a friendly technology mentor capable of:

- explaining beginner concepts
- guiding learners with hints
- adapting explanations
- maintaining a supportive teaching style

The evaluations also identified clear opportunities for future improvement, particularly around concise explanations and handling uncertainty.
