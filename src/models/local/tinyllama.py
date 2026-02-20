"""
tinyllama.py
---------
This file contains the implementation for reading and running the TinyLlama model.

The TinyLlama model is a lightweight version of the Llama model, designed for efficient inference on smaller devices.
"""
import os
from typing import List, Dict, Any
from src.models.local.interpreters.tinyllama.model import TinyLlamaModel

class TinyLlama:
    def __init__(self, config: Dict[str, Any] | None = None):
        """
        Local TinyLlama backend.

        The BackendAdapter will pass the full astra.config.json contents here.
        """
        if config is None:
            raise ValueError("TinyLlama backend requires configuration from astra.config.json")

        local_cfg = config.get("local_model_config", {})
        model_path = local_cfg.get("model_path")

        if not model_path:
            raise ValueError(
                "No model_path found in astra.config.json under local_model_config.\n"
                "Example:\n"
                '"local_model_config": {\n'
                '    "model_type": "tinyllama",\n'
                '    "model_path": "models/tinyllama/tinyllama.gguf",\n'
                '    "model_file_type": "gguf"\n'
                '}'
            )

        self.model = TinyLlamaModel({
            "model_path": model_path
        })

    def generate(self, system_prompt: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        return self.model.generate(system_prompt, history)
