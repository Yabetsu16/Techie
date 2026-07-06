"""
Conversation Service

Responsibility:
    Manages the current conversation between the learner and Techie.

Not Responsible For:
    - Generating responses
    - Prompt engineering
    - Calling the language model
    - Persisting conversations to disk

Used by:
    - main.py (Sprint 4)
    - Future TutorService
    - Future Web API

Design Goals:
    - Single responsibility
    - Easy to test
    - Easy to extend
    - In-memory conversation management
"""


class ConversationService:
    """
    Manage the conversation history between the learner and Techie.

    Stores messages in memory and provides them in the format expected by the language model.
    """

    def __init__(self, system_prompt: str) -> None:
        """Initialize an empty conversation history."""
        self._messages: list[dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]
        self._system_prompt = system_prompt

    def add_user_message(self, message: str) -> None:
        """Add a learner message to the conversation."""
        self._messages.append(self._create_message("user", message))

    def add_assistant_message(self, message: str) -> None:
        """Add Techie's response to the conversation."""
        self._messages.append(self._create_message("assistant", message))

    def get_messages(self) -> list[dict[str, str]]:
        """Return the current conversation history."""
        return self._messages.copy()

    def clear(self) -> None:
        """Clear the conversation history and keep the system prompt."""
        self._messages = [{"role": "system", "content": self._system_prompt}]

    def _create_message(self, role: str, content: str) -> dict[str, str]:
        """Create a conversation message."""
        return {"role": role, "content": content}
