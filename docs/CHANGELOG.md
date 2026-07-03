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
