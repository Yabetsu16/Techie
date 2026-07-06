"""
Tutor Service

Responsibility:
    Coordinates conversations between the learner,
    ConversationService, and LLMService.

Not Responsible For:
    - Managing conversation history
    - Communicating directly with the language model
    - User interaction

Used By:
    - main.py

Design Goals:
    - Single orchestration point
    - Easy to test
    - Easy to extend
"""

from app.services.conversation_service import ConversationService
from app.services.llm_service import LLMService


class TutorService:
    """
    Coordinates the teaching conversation between the learner,
    ConversationService, and LLMService.
    """

    def __init__(
        self, llm_service: LLMService, conversation_service: ConversationService
    ) -> None:
        """Initialize the tutor service."""
        self.llm_service = llm_service
        self.conversation_service = conversation_service

    def chat(self, message: str) -> str:
        """Process a learner message and return Techie's response.

        Args:
            message:
                The learner's message.

        Returns:
            Techie's response.
        """
        self.conversation_service.add_user_message(message)
        conversation_history = self.conversation_service.get_messages()
        response = self.llm_service.generate(conversation_history)
        self.conversation_service.add_assistant_message(response)

        return response
