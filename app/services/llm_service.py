"""
LLM Service

Responsibility:
    Acts as Techie's single gateway to all Large Language Model (LLM)
    providers through the OpenAI Python SDK.

Not Responsible For:
    - Prompt engineering
    - Conversation memory
    - User interaction
    - Teaching strategy
    - Response evaluation

Used By:
    - main.py (Sprint 2)
    - Future TutorService
    - Future QuizService
    - Future RAG components

Design Goals:
    - Provider agnostic
    - Easy to test
    - Easy to extend
    - Centralized LLM communication
"""

from openai import OpenAI

from app.config import config
from app.services.prompt_service import PromptService


class LLMService:
    """
    High-level interface for communicating with a language model.

    This class abstracts the underlying LLM provider from the rest of
    the application. Application modules should interact only with this
    service rather than directly using the OpenAI SDK.
    """

    def __init__(self) -> None:
        """Initialize the configured language model client."""
        self.client = OpenAI(base_url=config.base_url, api_key=config.api_key)

        self.model = config.model
        self.provider = config.provider

        prompt_service = PromptService()
        self.system_prompt = prompt_service.load_system_prompt()

    def chat(self, message: str) -> str:
        """
        Send a user message to the configured language model.

        Args:
            message:
                The learner's message.

        Returns:
            The assistant's response.
        """

        messages = self._build_messages(message)

        return self._generate(messages)

    def _build_messages(self, user_message: str) -> list[dict[str, str]]:
        """Build the message list sent to the language model."""

        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message},
        ]

    def _generate(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """Generate a response from the configured language model."""

        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=messages, max_completion_tokens=512
            )

            response_text = response.choices[0].message.content

            if response_text is None:
                return ""

            # Future:
            # response_text = self._post_process(response_text)

            return response_text

        except Exception as error:
            return "Sorry! I couldn't reach the language model.\n" f"Error: {error}"
