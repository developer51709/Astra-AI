"""
openai_generic.py
---------
Implementation for a generic OpenAI-compatible API.
"""
import os
from typing import List, Dict, Any
from openai import OpenAI

class OpenAIGeneric:
    def __init__(self, config: Dict[str, Any]):
        cloud_cfg = config.get("cloud_model_config", {})
        self.model = cloud_cfg.get("model_name", "gpt-4")
        api_key = cloud_cfg.get("model_api_key") or os.environ.get("OPENAI_API_KEY")
        base_url = cloud_cfg.get("model_api_endpoint") or os.environ.get("OPENAI_BASE_URL")

        if not api_key:
            raise ValueError("OpenAI API key not found in config or environment (OPENAI_API_KEY)")

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def generate(self, system_prompt: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(history)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            reply = response.choices[0].message.content or ""
        except Exception as e:
            reply = f"Error from OpenAI backend: {e}"

        return {
            "response": reply,
            "metadata": {
                "backend": "openai_generic",
                "model": self.model,
            }
        }
