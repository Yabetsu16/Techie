"""
Application Configuration

Responsibility:
    Loads and centralizes application configuration from environment
    variables.

Not Responsible For:
    - Business logic
    - Validation of user input
    - Creating application services

Used By:
    - LLMService
    - Future application services

Design Goals:
    - Single source of truth
    - Environment-driven configuration
    - Immutable application settings
"""

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    provider: str = os.getenv("PROVIDER", "Ollama Local")
    model: str = os.getenv("MODEL", "qwen3.5:9b")
    base_url: str = os.getenv("BASE_URL", "http://localhost:11434/v1")
    api_key: str = os.getenv("API_KEY", "ollama")


# Singleton configuration instance used throughout the application.
config = Settings()
