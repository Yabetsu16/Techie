# Changelog

All notable changes to **Techie** will be documented in this file.

The format is inspired by **Keep a Changelog**, and the project follows **Semantic Versioning**.

---

## [0.1.0] - Apprentice

### Added

- Initialized the Techie project repository.
- Created the initial project folder structure.
- Added the `app`, `services`, `prompts`, `docs`, and `tests` packages.
- Added `__init__.py` files to define Python packages.
- Created the initial `README.md`.
- Defined Techie's vision, mission, teaching philosophy, manifesto, and product identity.
- Added the initial `requirements.txt`.
- Added `.gitignore` for Python and AI development.
- Created the project environment configuration with `.env`.

### Planned

- Implement the LLM service.
- Connect Techie to Ollama.
- Send the first prompt to a local language model.

---

## [0.2.0] - First Contact

### 🎉 Milestone

Techie successfully completed its first end-to-end conversation using a locally hosted open-source LLM through Ollama.

### Added

- Interactive command-line REPL
- `LLMService` abstraction for LLM communication
- Provider-agnostic architecture using the OpenAI Python SDK
- Ollama Local support
- Environment-based configuration (`.env`)
- Centralized application constants
- Welcome banner displayed at startup
- Runtime display of active provider and model
- `VERSION` file
- MIT License

### Architecture

- Modular project structure
- Dedicated `services` package
- Dedicated `prompts` package
- Immutable application configuration using a frozen dataclass
- Singleton configuration object
- Separation of responsibilities between application entry point and services

### Documentation

- Project README
- Getting Started guide
- Architecture documentation
- Engineering Decisions document
- Techie's Promise
- Teaching philosophy and project values

### Engineering

- Git repository initialized
- Virtual environment support
- `.gitignore` for Python projects
- Dependency management through `requirements.txt`
- Consistent module-level docstrings
- Type hints throughout the application

### Validation

- Successfully connected to Ollama Local
- Successfully generated the first AI response
- Established the baseline evaluation for Techie's teaching quality

---

## [0.3.0] - Sprint 3

### Added

- PromptService
- External system prompt loading
- Techie's teaching identity
- Teaching philosophy
- Teaching style
- Communication guidelines
- Sprint evaluation framework
- Sprint evaluation logs
- Sprint retrospective
- Ruff configuration
- VS Code workspace settings

### Changed

- Refactored `LLMService`
- Extracted message building into a dedicated method
- Extracted response generation into a dedicated method
- Improved project architecture for future conversation memory
- Improved project documentation

### Evaluated

Completed six structured teaching evaluations.

Overall Score:

159 / 180 (88.3%)

---

## [0.4.0] - Conversation Memory

### Added

- Introduced `ConversationService` to manage in-memory conversation history.
- Added support for storing:
  - System messages
  - User messages
  - Assistant messages
- Implemented conversation clearing while preserving the system prompt.
- Added reusable message creation helper.
- Added `TutorService` to orchestrate conversations between the learner, conversation history, and language model.
- Refactored `LLMService` to accept the complete conversation history instead of a single user message.
- Moved system prompt ownership from `LLMService` to `ConversationService`.
- Updated `main.py` to initialize application services using dependency injection.

### Testing

- Added unit tests for `ConversationService`.
- Added pytest fixtures for cleaner test setup.
- Verified:
  - Empty conversation initialization
  - User message storage
  - Assistant message storage
  - Message ordering
  - Conversation clearing
  - Defensive copying of conversation history

### Debugging

- Investigated multi-turn conversation failures.
- Verified that conversation history was correctly passed to the LLM.
- Identified a compatibility issue with `qwen3.5:9b` through Ollama's OpenAI-compatible API, where multi-turn conversations occasionally returned empty responses.
- Confirmed that `llama3.2` correctly supports conversation memory with the current architecture.

### Architecture Improvements

- Strengthened separation of responsibilities:
  - `ConversationService` owns conversation history.
  - `TutorService` coordinates application flow.
  - `LLMService` focuses solely on communicating with the language model.
