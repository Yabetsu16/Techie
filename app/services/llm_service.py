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

    def generate(self, messages: list[dict[str, str]]) -> str:
        """
        Generate a response from the configured language model.

        Args:
            messages:
                The conversation history sent to the language model.

        Returns:
            The generated response text.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=messages
            )

            message = response.choices[0].message

            if message.content is None:
                raise RuntimeError("The model returned an empty response.")

            # Future:
            # response_text = self._post_process(response_text)

            return message.content

        except Exception as error:
            return "Sorry! I couldn't reach the language model.\n" f"Error: {error}"
