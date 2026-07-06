import pytest

from app.services.conversation_service import ConversationService
from app.services.tutor_service import TutorService

from tests.fakes.fake_llm_service import FakeLLMService


@pytest.fixture
def conversation() -> ConversationService:
    """Return a fresh conversation."""

    return ConversationService("System prompt")


@pytest.fixture
def fake_llm() -> FakeLLMService:
    """Return a fake language model."""

    return FakeLLMService()


@pytest.fixture
def tutor(conversation: ConversationService, fake_llm: FakeLLMService) -> TutorService:
    """Return a configured tutor service."""

    return TutorService(fake_llm, conversation)
