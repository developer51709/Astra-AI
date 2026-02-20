"""
tinyllama.py
---------
This file contains the implementation for reading and running the TinyLlama model.

The TinyLlama model is a lightweight version of the Llama model, designed for efficient inference on smaller devices.
"""
import os
from typing import List, Dict, Any
from .interpreters.tinyllama.model import TinyLlamaModel

class TinyLlama:
    def __init__(self):
        # Load config from environment or defaults
        model_path = os.environ.get("ASTRA_LOCAL_MODEL_PATH", "tinyllama.gguf")

        self.model = TinyLlamaModel({
            "model_path": model_path
        })

    def generate(self, system_prompt: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        return self.model.generate(system_prompt, history)