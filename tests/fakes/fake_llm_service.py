"""
Fake LLM Service

Used for unit testing without calling a real language model.
"""


class FakeLLMService:
    """A fake language model used for unit testing."""

    def __init__(self, response: str = "Hello from Techie!") -> None:
        self.response = response
        self.messages: list[dict[str, str]] = []

    def generate(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """Return the configured response."""
        self.messages = messages
        return self.response
