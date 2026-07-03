"""
Techie Application Entry Point

Responsibility:
    Starts the application and manages the command-line interaction
    between the learner and Techie.

Not Responsible For:
    - Communicating with language models
    - Prompt engineering
    - Business logic

Uses:
    - LLMService

Current Interface:
    Command-Line REPL

Future Interfaces:
    - FastAPI
    - Web UI
    - Desktop UI
"""

from app.services.llm_service import LLMService
from app.constants import EXIT_COMMANDS, WELCOME_MESSAGE


def get_llm_service() -> LLMService:
    """Return the application's configured LLM service."""
    return LLMService()


def main() -> None:
    """Start Techie's interactive command-line REPL."""

    llm = get_llm_service()

    print(WELCOME_MESSAGE)
    print(f"Provider: {llm.provider}")
    print(f"Model: {llm.model}")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() in EXIT_COMMANDS:
            print("\nTechie: Happy learning! 👋")
            break

        response = llm.chat(user_input)

        print(f"\nTechie: {response}")


if __name__ == "__main__":
    main()
