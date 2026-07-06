# Sprint 4 Summary

## Goal

Introduce conversation memory so Techie can remember previous messages during a learning session.

---

## Accomplishments

### Conversation Management

Implemented a dedicated `ConversationService` responsible for managing the conversation history.

The service now:

- stores the system prompt
- stores user messages
- stores assistant messages
- returns conversation history in OpenAI message format
- resets conversations while preserving the system prompt

---

### Tutor Service

Introduced `TutorService` as the orchestration layer between:

- ConversationService
- LLMService

The tutor service is now responsible for:

1. receiving learner messages
2. updating conversation history
3. requesting responses from the language model
4. storing assistant responses

---

### LLM Refactoring

`LLMService` was simplified.

Responsibilities now include:

- communicating with the configured language model
- generating responses from conversation history

Responsibilities removed:

- conversation management
- system prompt ownership
- message construction

---

### Testing

Added unit tests covering:

- conversation initialization
- adding user messages
- adding assistant messages
- message ordering
- conversation clearing
- defensive copying

All tests currently pass.

---

### Debugging

During testing, conversation memory appeared to fail.

Investigation showed:

- ConversationService behaved correctly.
- TutorService correctly passed conversation history.
- LLMService correctly sent all messages.

The issue was traced to the local model (`qwen3.5:9b`) through Ollama's OpenAI-compatible API.

Switching to `llama3.2` confirmed that the architecture works correctly.

---

## Current Architecture

main.py
↓
TutorService
├── ConversationService
└── LLMService
↓
OpenAI SDK
↓
Ollama

The responsibilities are now clearly separated, making future features easier to implement.

---

## Sprint Status

Milestone 2 completed successfully.

Conversation memory is fully functional using compatible language models.

Techie now supports multi-turn conversations while maintaining clean architecture principles.

## Project Metrics

Services: 5

- PromptService
- LLMService
- ConversationService
- TutorService
- Config

Unit Tests: 6 (all passing)

Architecture

✓ Dependency Injection
✓ Service Layer
✓ Conversation Memory
✓ Clean Separation of Responsibilities

Current Capabilities

✓ Single-turn tutoring
✓ Multi-turn conversations
✓ System prompt loading
✓ Local LLM support
✓ Conversation history
