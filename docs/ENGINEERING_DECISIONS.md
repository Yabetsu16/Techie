# Engineering Decisions

This document records the architectural and technical decisions made during the development of Techie.

---

## ED-001 — Use Ollama for Local LLM Inference

**Status:** Accepted

### Context

Techie is designed as a portfolio project that should be free to develop and run without relying on paid AI APIs.

### Decision

Use Ollama as the local inference engine for running open-source language models.

### Rationale

- No API costs
- Works offline
- Privacy-friendly
- Easy model switching
- Excellent for learning AI engineering fundamentals

### Consequences

- Requires users to install Ollama
- Hardware-dependent performance
- Limited by local GPU resources

---

## ED-002 — Use the OpenAI Python SDK as the LLM Client

**Status:** Accepted

### Context

Techie is designed to support multiple Large Language Model (LLM) providers over time while remaining free to develop during the MVP phase.

Although Ollama provides its own Python client, many local and cloud inference providers expose an OpenAI-compatible API. Using the OpenAI Python SDK allows Techie to communicate with these providers through a consistent interface.

Examples include:

- Ollama
- LM Studio
- vLLM
- OpenRouter
- Groq
- OpenAI
- Together AI

### Decision

Use the official OpenAI Python SDK as the client library for all LLM communication.

During development, the SDK will connect to Ollama's OpenAI-compatible endpoint:

- Base URL: `http://localhost:11434/v1`
- API Key: Placeholder (required by the SDK but ignored by Ollama)

### Rationale

Using the OpenAI SDK provides several advantages:

- Standardized API across multiple providers.
- Easier migration between local and cloud inference engines.
- Industry-standard client library.
- Cleaner abstraction for future provider switching.
- Supports advanced features such as streaming, structured outputs, and function calling.

### Consequences

#### Positive

- Provider-agnostic architecture.
- Minimal code changes when switching providers.
- Easier experimentation with different LLM backends.
- Better long-term maintainability.

#### Negative

- Requires understanding OpenAI-compatible APIs.
- Some provider-specific features may require custom implementations.
- Adds a small abstraction layer over Ollama's native client.

### Alternatives Considered

#### Ollama Python SDK

Pros

- Simple to use.
- Designed specifically for Ollama.
- Excellent for small local projects.

Cons

- Tightly coupled to Ollama.
- Harder to migrate to other providers.

### Decision Outcome

Accepted.

Techie will standardize on the OpenAI Python SDK while using Ollama as the initial local inference provider.

The rest of the application should remain unaware of which provider is being used.

---

## ED-003 — Depend on Service Abstractions Instead of SDKs

**Status:** Accepted

### Context

As Techie grows, multiple modules (conversation memory, quizzes, tutoring, RAG, etc.) will require access to a Large Language Model.

Allowing each module to communicate directly with the OpenAI SDK would tightly couple the application to a specific implementation.

### Decision

Introduce an `LLMService` responsible for all interactions with language models.

Application modules should communicate only with `LLMService` and must never call the OpenAI SDK directly.

### Rationale

This decision follows the Dependency Inversion Principle.

By centralizing LLM communication:

- Provider changes remain isolated.
- Configuration is centralized.
- Logging and retries can be implemented once.
- Future caching can be added transparently.
- Unit testing becomes significantly easier.

### Consequences

#### Positive

- Cleaner architecture.
- Easier provider migration.
- Reduced duplication.
- Improved maintainability.
- Better testability.

#### Negative

- Introduces one additional abstraction layer.
- Slightly more code during the MVP.

### Decision Outcome

Accepted.

`LLMService` will become the single gateway for all language model interactions throughout Techie.

---

## ED-004 — Configuration-Driven LLM Provider Selection

**Status:** Accepted

### Context

Techie should support multiple inference providers without requiring application code changes.

The project will initially use Ollama Local during development while also supporting Ollama Cloud for remote inference.

Future providers may include OpenAI, LM Studio, vLLM, and OpenRouter.

### Decision

Provider selection will be determined entirely through configuration.

The application will instantiate the same `LLMService` regardless of the selected provider.

Only configuration values such as `BASE_URL`, `API_KEY`, and `MODEL_NAME` should change.

### Rationale

- Eliminates provider-specific logic from the application.
- Simplifies experimentation with different models.
- Encourages environment-based configuration.
- Keeps deployment flexible.

### Consequences

#### Positive

- No code changes when switching providers.
- Cleaner deployments.
- Easier local and cloud development.
- Simpler testing across providers.

#### Negative

- Different providers may have provider-specific limitations.
- Some advanced features may require conditional implementations.

### Decision Outcome

Accepted.

Techie will treat the language model provider as configuration rather than application logic.

---

## ED-005 — Document Intent, Not Implementation

**Status:** Accepted

### Context

As Techie grows, maintaining readability becomes increasingly important.

Comments and docstrings that merely repeat the code provide little value and quickly become outdated.

### Decision

Docstrings should explain the purpose, responsibilities, and design intent of a module, class, or function.

Inline comments should explain _why_ a decision was made rather than _what_ the code is doing.

### Rationale

- Improves maintainability.
- Helps future contributors understand architectural intent.
- Reduces redundant documentation.
- Encourages self-documenting code.

### Decision Outcome

Accepted.

Documentation should complement the code rather than duplicate it.

---

## ED-006 — Favor Convention Over Configuration

**Status:** Accepted

### Decision

Techie will follow widely accepted Python conventions whenever possible instead of introducing project-specific patterns.

Examples include:

- Standard project structure
- Conventional environment variable names
- PEP 8 formatting
- Industry-standard SDKs
- Minimal dependencies

### Rationale

Following conventions reduces cognitive load, improves onboarding, and makes the project feel familiar to other Python developers.

---

## ED-007 — Keep Services Focused

**Status:** Accepted

### Context

As Techie grows, services could accumulate unrelated responsibilities such as prompt construction, conversation memory, logging, and business logic.

### Decision

Each service should own one primary responsibility.

Examples:

- `LLMService` — Communication with language models
- `TutorService` — Teaching strategy
- `MemoryService` — Conversation history
- `QuizService` — Quiz generation

### Rationale

Single-purpose services are easier to understand, test, and extend.

### Outcome

Future features should be implemented by introducing new services rather than expanding existing ones beyond their core responsibility.
