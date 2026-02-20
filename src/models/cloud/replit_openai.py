"""
replit_openai.py
---------
This file contains the implementation for using Replit's OpenAI-compatible API via Replit's AI Integrations service.
"""
import os
from typing import List, Dict, Any
from openai import OpenAI

class ReplitOpenAI:
    def __init__(self):
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        self.model = "gpt-5"

        # Verify the environment variables exist
        if not os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY") or not os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL"):
            raise ValueError("AI_INTEGRATIONS_OPENAI_API_KEY or AI_INTEGRATIONS_OPENAI_BASE_URL environment variables are not set.\nPlease verify that you are running this in a Replit environment with the AI Integrations service enabled. If you are not running this in a Replit environment, please set a different backend in the astra.config.json file.")

        # This is using Replit's AI Integrations service, which provides
        # OpenAI-compatible API access without requiring your own OpenAI API key.
        self.client = OpenAI(
            api_key=os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY"),
            base_url=os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL"),
        )

    def generate(self, system_prompt: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Generates a response using OpenAI chat completions.

        Parameters:
            system_prompt (str): The system prompt defining Astra AI's identity.
            history (list): Conversation history as a list of role/content dicts.

        Returns:
            dict: {
                "response": str,
                "metadata": dict
            }
        """
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(history)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_completion_tokens=8192,
            )
            reply = response.choices[0].message.content or ""
        except Exception as e:
            reply = f"I encountered an error processing your request: {e}"

        return {
            "response": reply,
            "metadata": {
                "backend": "openai",
                "model": self.model,
            }
        }