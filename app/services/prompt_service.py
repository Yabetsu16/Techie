"""
Prompt Service

Responsibility:
    Loads prompt templates from disk.

Not Responsible For:
    - Calling language models
    - Prompt engineering
    - Conversation management
    - Business logic

Used By:
    - LLMService

Design Goals:
    - Keep prompts outside Python code
    - Easy to extend
    - Easy to test
"""

from pathlib import Path


class PromptService:
    """Loads prompt templates from disk."""

    def __init__(self) -> None:
        """Initialize the prompt directory."""

        self.prompt_directory = Path(__file__).parent.parent / "prompts"

    def load_system_prompt(self) -> str:
        """Load Techie's system prompt.

        Return:
            The system prompt as a string.
        """

        prompt_path = self.prompt_directory / "system_prompt.md"

        return prompt_path.read_text(encoding="utf-8").strip()
