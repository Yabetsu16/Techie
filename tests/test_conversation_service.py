import pytest
from app.services.conversation_service import ConversationService


@pytest.fixture
def conversation() -> ConversationService:
    """Create a fresh conversation for each test."""
    return ConversationService("Test system prompt")


def test_new_conversation_start_empty(conversation: ConversationService) -> None:
    """A new conversation should have no messages."""
    assert conversation.get_messages() == [
        {"role": "system", "content": "Test system prompt"}
    ]


def test_add_user_message(conversation: ConversationService) -> None:
    """Adding a user message should store it in the conversation."""
    conversation.add_user_message("Hello")

    assert conversation.get_messages() == [
        {"role": "system", "content": "Test system prompt"},
        {"role": "user", "content": "Hello"},
    ]


def test_add_assistant_message(conversation: ConversationService) -> None:
    """Adding an assistant message should store it in the conversation."""
    conversation.add_assistant_message("Hi!")

    assert conversation.get_messages() == [
        {"role": "system", "content": "Test system prompt"},
        {"role": "assistant", "content": "Hi!"},
    ]


def test_messages_are_returned_in_order(conversation: ConversationService) -> None:
    """Messages should remain in the order they were added."""
    conversation.add_user_message("Hello")
    conversation.add_assistant_message("Hi!")
    conversation.add_user_message("How are you?")

    assert conversation.get_messages() == [
        {"role": "system", "content": "Test system prompt"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi!"},
        {"role": "user", "content": "How are you?"},
    ]


def test_clear_removes_all_messages(conversation: ConversationService) -> None:
    """Clearing the conversation should remove every message."""
    conversation.add_user_message("Hello")
    conversation.add_assistant_message("Hi!")

    conversation.clear()

    assert conversation.get_messages() == [
        {"role": "system", "content": "Test system prompt"},
    ]


def test_get_messages_returns_a_copy(conversation: ConversationService) -> None:
    """Returned messages should not modify the internal conversation."""
    conversation.add_user_message("Hello")

    messages = conversation.get_messages()

    messages.clear()

    assert conversation.get_messages() == [
        {"role": "system", "content": "Test system prompt"},
        {"role": "user", "content": "Hello"},
    ]
