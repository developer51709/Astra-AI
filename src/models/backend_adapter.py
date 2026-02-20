"""
backend_adapter.py
---------
The BackendAdapter abstracts the underlying model implementation, allowing
Astra AI to work with both local models and API-based services.

This module handles:
- Formatting requests for different backends
- Parsing responses from different backends
- Managing backend-specific configurations
- Providing a consistent interface to the Engine

The BackendAdapter decides what backend to use based on the configuration and then routes requests to the appropriate backend in either the local or cloud subfolder and does not handle the requests directly as it is just a router.
"""

import os
import json
from typing import Dict, Any, List

from src.models.cloud.replit_openai import ReplitOpenAI
from src.models.local.tinyllama import TinyLlama

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "astra.config.json")


class BackendAdapter:
    """
    Provides a unified interface for generating model responses.
    Decides what backend to use based on the configuration.
    Routes to either the local or cloud subfolder based on the config set in the astra.config.json file.
    """
    def __init__(self, config: Dict[str, Any] | None = None):
        if config is not None:
            self.config = config
        else:
            with open(CONFIG_PATH, "r") as f:
                self.config = json.load(f)
        if self.config["local_or_cloud"] == "local":
            self.backend = TinyLlama()
        elif self.config["local_or_cloud"] == "cloud":
            self.backend = ReplitOpenAI()
        else:
            raise ValueError(f"Unknown backend type: {self.config['local_or_cloud']}")

    def generate(self, system_prompt: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        return self.backend.generate(system_prompt, history)

