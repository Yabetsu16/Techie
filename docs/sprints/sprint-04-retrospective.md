# Sprint 4 Retrospective

## What Went Well

### Architecture

The application architecture became significantly cleaner.

Introducing dedicated services improved separation of concerns and reduced coupling between components.

Each service now has a single, well-defined responsibility.

---

### Test-Driven Development

Unit tests quickly identified implementation mistakes during development.

The tests also made refactoring much safer by verifying that behavior remained correct.

---

### Debugging Process

Instead of assuming the architecture was incorrect, the debugging process focused on gathering evidence.

Printing the conversation history confirmed that:

- messages were stored correctly
- messages were sent correctly
- the orchestration flow worked as intended

This avoided unnecessary redesigns.

---

### Lessons Learned

Not every bug originates from application code.

External components such as local language models or API compatibility layers can introduce unexpected behavior.

Verifying assumptions before making architectural changes saved significant development time.

---

## Challenges

The primary challenge was diagnosing why multi-turn conversations returned empty responses.

Initially, the issue appeared to be related to conversation memory.

After systematic debugging, the root cause was identified as a compatibility issue between:

- qwen3.5:9b
- Ollama's OpenAI-compatible endpoint

---

## Improvements

Future debugging should continue following an evidence-based approach:

1. Verify application state.
2. Verify requests.
3. Verify responses.
4. Only then investigate architecture.

This reduces unnecessary changes and makes problems easier to isolate.

---

## Technical Debt

Current observations:

- Add graceful handling for empty model responses.
- Consider automatic retries for empty completions.
- Add compatibility notes for supported local models.

These improvements are not required for Sprint 4 but would improve robustness.

---

## Overall Assessment

Sprint 4 successfully transformed Techie from a single-turn chatbot into a conversational tutor capable of maintaining context across multiple learner interactions.

This architectural foundation prepares the project for future features such as:

- persistent conversations
- long-term learner memory
- RAG
- quizzes
- learning progress tracking
