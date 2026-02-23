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
from src.models.cloud.openai_generic import OpenAIGeneric
from src.models.local.tinyllama import TinyLlama
from src.models.local.generic_gguf import GenericGGUF

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
            local_cfg = self.config.get("local_model_config", {})
            model_type = local_cfg.get("model_type", "tinyllama")
            
            try:
                if model_type == "tinyllama":
                    self.backend = TinyLlama(self.config)
                elif model_type == "generic_gguf":
                    self.backend = GenericGGUF(self.config)
                else:
                    print(f"[Astra] Unknown local model type: {model_type}. Using TinyLlama.")
                    self.backend = TinyLlama(self.config)
            except Exception as e:
                print(f"[Astra] Local backend failed to load: {e}")
                print("[Astra] Falling back to cloud backend.")
                self.backend = ReplitOpenAI()
        elif self.config["local_or_cloud"] == "cloud":
            cloud_cfg = self.config.get("cloud_model_config", {})
            model_type = cloud_cfg.get("model_type", "replit_openai")
            
            if model_type == "replit_openai":
                self.backend = ReplitOpenAI()
            elif model_type == "openai_generic":
                self.backend = OpenAIGeneric(self.config)
            else:
                print(f"[Astra] Unknown cloud model type: {model_type}. Using Replit OpenAI.")
                self.backend = ReplitOpenAI()
        else:
            raise ValueError(f"Unknown backend type: {self.config['local_or_cloud']}")

    def generate(self, system_prompt: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        return self.backend.generate(system_prompt, history)
