import os
from dotenv import load_dotenv

load_dotenv()


class ConfigError(Exception):
    """Custom exception for configuration-related errors"""
    pass


def get_gemini_api_key() -> str:
    """Retrieve the Gemini API key from the environment."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ConfigError(
            "Gemini API key not found in environment configuration.")
    return api_key
