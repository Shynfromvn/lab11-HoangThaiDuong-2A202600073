"""
Lab 11 - Configuration & API Key Setup
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm


DEFAULT_OPENAI_MODEL = "gpt-4o-mini"


def setup_api_key():
    """Load OpenAI settings from .env or environment."""
    project_root = Path(__file__).resolve().parents[2]
    load_dotenv(project_root / ".env")

    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = input("Enter OpenAI API Key: ")

    os.environ.setdefault("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
    print(f"OpenAI API key loaded. Model: {os.environ['OPENAI_MODEL']}")


def get_openai_model_name() -> str:
    """Return the raw OpenAI model name for SDK and NeMo use."""
    return os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)


def build_adk_model() -> LiteLlm:
    """Create an ADK LiteLLM wrapper backed by OpenAI."""
    return LiteLlm(model=f"openai/{get_openai_model_name()}")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
