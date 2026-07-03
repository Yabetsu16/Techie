# Techie Architecture

> **Think. Learn. Build.**

This document describes the architecture of Techie and the reasoning behind the major technical decisions.

The goal is to keep the application simple, maintainable, and easy to extend as new features are added.

---

# Design Principles

Techie follows a few core engineering principles.

## 1. Separation of Responsibilities

Each module should have one clear responsibility.

| Component    | Responsibility                     |
| ------------ | ---------------------------------- |
| `main.py`    | Application entry point            |
| `config.py`  | Application configuration          |
| `LLMService` | Communication with language models |
| `prompts/`   | Prompt templates                   |
| `tests/`     | Unit and integration tests         |

---

## 2. Configuration over Hardcoding

Application behavior should be controlled through configuration rather than hardcoded values.

Environment variables determine:

- Model
- API Key
- Base URL

This allows Techie to switch providers without changing code.

---

## 3. Depend on Abstractions

Application modules should communicate with `LLMService`.

They should never communicate directly with the OpenAI SDK.

This keeps the application independent from any specific provider.

---

# High-Level Architecture

```text
                +----------------------+
                |      main.py         |
                | Application Entry    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     LLMService       |
                | Business Interface   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    OpenAI SDK        |
                +----------+-----------+
                           |
                           v
            OpenAI-Compatible API Endpoint
                           |
      +----------+----------+----------+----------+
      |          |          |          |          |
      v          v          v          v          v
 Ollama     Ollama Cloud  LM Studio   vLLM     OpenAI
```

---

# Project Structure

```text
techie/

├── app/
│   ├── prompts/
│   ├── services/
│   │   └── llm.py
│   ├── config.py
│   ├── main.py
│   └── __init__.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── ENGINEERING_DECISIONS.md
│   └── PRODUCT_VISION.md
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── README.md
├── VERSION
└── requirements.txt
```

---

# Component Responsibilities

## main.py

Responsible for:

- Starting Techie
- Managing the REPL
- Handling user interaction

It should never:

- Call the OpenAI SDK directly
- Read environment variables
- Build prompts

---

## config.py

Responsible for:

- Loading environment variables
- Creating a single configuration object
- Providing configuration to the application

This file becomes the single source of truth for application configuration.

---

## LLMService

Responsible for:

- Sending messages to the language model
- Receiving responses
- Abstracting the underlying provider

Future capabilities may include:

- Streaming
- Structured outputs
- Tool calling
- Retry logic
- Logging
- Response caching

---

## prompts/

Contains reusable prompt templates.

Future examples:

- Tutor Prompt
- Quiz Prompt
- Code Review Prompt
- Socratic Teaching Prompt

---

## tests/

Contains unit and integration tests.

Future tests include:

- LLMService
- Prompt Builder
- Tutor Service
- Conversation Memory

---

# Configuration Flow

```text
.env
      |
      v
config.py
      |
      v
config
      |
      +---------------------+
      |                     |
      v                     v
LLMService              Future Services
```

Configuration should only be loaded once.

Application modules should never call `os.getenv()` directly.

---

# Current Request Flow

```text
User

↓

main.py

↓

LLMService

↓

OpenAI SDK

↓

Configured Provider

↓

Response

↓

LLMService

↓

main.py

↓

User
```

---

# Current LLM Provider

The current implementation uses:

- OpenAI Python SDK
- Ollama Local (default)

Future providers will require only configuration changes.

---

# Future Providers

Techie is designed to support multiple OpenAI-compatible providers.

Examples include:

- Ollama Local
- Ollama Cloud
- LM Studio
- OpenAI
- OpenRouter
- Groq
- Together AI
- vLLM

No application code should need to change when switching providers.

---

# Planned Architecture Evolution

## Phase 1

```
main.py

↓

LLMService

↓

LLM
```

---

## Phase 2

```
main.py

↓

TutorService

↓

LLMService

↓

LLM
```

---

## Phase 3

```
main.py

↓

TutorService

↓

Prompt Builder

↓

LLMService

↓

LLM
```

---

## Phase 4

```
main.py

↓

TutorService

↓

Prompt Builder

↓

Conversation Memory

↓

LLMService

↓

RAG

↓

LLM
```

---

# Architecture Goals

The architecture should remain:

- Simple
- Modular
- Testable
- Provider-agnostic
- Easy to extend
- Beginner-friendly

Every new feature should integrate naturally into the existing architecture without requiring major rewrites.

---

# Philosophy

> **Techie should never depend on a specific AI provider.**

The application should depend only on its own services.

Everything else should be replaceable.
