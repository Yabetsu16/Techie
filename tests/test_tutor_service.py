from app.services.conversation_service import ConversationService
from app.services.tutor_service import TutorService
from tests.fakes.fake_llm_service import FakeLLMService


def test_chat_returns_llm_response(tutor: TutorService) -> None:
    response = tutor.chat("Hello")

    assert response == "Hello from Techie!"


def test_chat_stores_user_message(
    tutor: TutorService, conversation: ConversationService
) -> None:
    """TutorService should store the learner message."""
    tutor.chat("Hello")

    assert conversation.get_messages()[1] == {"role": "user", "content": "Hello"}


def test_chat_stores_assistant_message(
    tutor: TutorService, conversation: ConversationService
) -> None:
    """TutorService should store the assistant response."""
    tutor.chat("Hello")

    assert conversation.get_messages()[2] == {
        "role": "assistant",
        "content": "Hello from Techie!",
    }


def test_chat_updates_conversation_history(
    tutor: TutorService, conversation: ConversationService
) -> None:
    """TutorService should update the conversation history."""
    tutor.chat("Hello")

    assert conversation.get_messages() == [
        {"role": "system", "content": "System prompt"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hello from Techie!"},
    ]


def test_chat_sends_conversation_to_llm(
    tutor: TutorService, fake_llm: FakeLLMService
) -> None:
    """TutorService should send the conversation history to the LLM."""
    tutor.chat("Hello")

    assert fake_llm.messages == [
        {"role": "system", "content": "System prompt"},
        {"role": "user", "content": "Hello"},
    ]
