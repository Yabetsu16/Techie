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

from app.services.tutor_service import TutorService
from app.services.conversation_service import ConversationService
from app.services.llm_service import LLMService
from app.constants import EXIT_COMMANDS, WELCOME_MESSAGE
from app.services.prompt_service import PromptService

prompt_service = PromptService()

system_prompt = prompt_service.load_system_prompt()

conversation_service = ConversationService(system_prompt)

llm_service = LLMService()

tutor_service = TutorService(llm_service, conversation_service)


def main() -> None:
    """Start Techie's interactive command-line REPL."""

    print(WELCOME_MESSAGE)
    print(f"Provider: {llm_service.provider}")
    print(f"Model: {llm_service.model}")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() in EXIT_COMMANDS:
            print("\nTechie: Happy learning! 👋")
            break

        response = tutor_service.chat(user_input)

        print(f"\nTechie: {response}")


if __name__ == "__main__":
    main()
