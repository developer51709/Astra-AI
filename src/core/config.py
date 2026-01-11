"""
config.py
---------
Centralized configuration management for Astra AI.

This module handles:
- Loading environment variables
- Defining default settings
- Loading the system prompt from the prompts directory
- Providing a single source of truth for backend configuration

The goal is to keep configuration clean, transparent, and easy to extend.
"""

import os
from pathlib import Path
from typing import Dict, Any


# ---------------------------------------------------------------------------
# 1. DEFAULT CONFIGURATION VALUES
# ---------------------------------------------------------------------------
# These values act as fallbacks if environment variables are not set.
# They can be expanded later as Astra AI grows.

DEFAULT_CONFIG = {
    "MODEL_BACKEND": "local",          # "local", "api", or custom backend name
    "MODEL_NAME": "default-model",     # Placeholder until backends are implemented
    "API_KEY": None,                   # Used only if backend requires authentication
    "SYSTEM_PROMPT_PATH": "prompts/system_prompt.md",
}


# ---------------------------------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------------------------
# This function merges environment variables with default config values.
# It allows users to override settings without modifying the codebase.

def load_config() -> Dict[str, Any]:
    """
    Loads configuration values from environment variables,
    falling back to DEFAULT_CONFIG when necessary.

    Returns:
        dict: A dictionary containing all configuration settings.
    """
    config = DEFAULT_CONFIG.copy()

    # Override defaults with environment variables if present.
    config["MODEL_BACKEND"] = os.getenv("ASTRA_MODEL_BACKEND", config["MODEL_BACKEND"])
    config["MODEL_NAME"] = os.getenv("ASTRA_MODEL_NAME", config["MODEL_NAME"])
    config["API_KEY"] = os.getenv("ASTRA_API_KEY", config["API_KEY"])
    config["SYSTEM_PROMPT_PATH"] = os.getenv("ASTRA_SYSTEM_PROMPT_PATH", config["SYSTEM_PROMPT_PATH"])

    return config


# ---------------------------------------------------------------------------
# 3. LOAD SYSTEM PROMPT FROM FILE
# ---------------------------------------------------------------------------
# The system prompt defines Astra AI's identity, tone, and safety rules.
# Keeping it external makes it easy to update without touching code.

def load_system_prompt() -> str:
    """
    Loads the system prompt text from the file specified in configuration.

    Returns:
        str: The full system prompt as a string.

    Raises:
        FileNotFoundError: If the system prompt file does not exist.
    """
    config = load_config()
    prompt_path = Path(config["SYSTEM_PROMPT_PATH"])

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"System prompt file not found at: {prompt_path}. "
            "Make sure the path is correct or update ASTRA_SYSTEM_PROMPT_PATH."
        )

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------
# 4. OPTIONAL: SIMPLE CONFIG ACCESSOR
# ---------------------------------------------------------------------------
# This helper allows other modules to access config values easily.

def get(setting: str) -> Any:
    """
    Retrieves a single configuration value.

    Example:
        backend = get("MODEL_BACKEND")

    Parameters:
        setting (str): The name of the configuration key.

    Returns:
        Any: The value of the requested setting.
    """
    config = load_config()
    return config.get(setting)
