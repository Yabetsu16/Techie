"""
LLM Protocol

Defines the interface required by any language model implementation.
"""

from typing import Protocol


class LLMProtocol(Protocol):
    """Interface for language model services."""

    def generate(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """Generate a response from the conversation history."""
        ...
