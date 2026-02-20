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

This file is intentionally modular to allow easy addition of new backends.
"""

from typing import Dict, Any


class BackendAdapter:
    """
    Provides a unified interface for generating model responses.

    Currently uses a simple template-based response system for demonstration.
    Can be extended to support local models or API-based services.
    """

    def __init__(self, backend_type: str = "local"):
        self.backend_type = backend_type

    def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Generates a response from the configured backend.

        Parameters:
            prompt (str): The full assembled prompt including system prompt
                          and conversation history.

        Returns:
            dict: {
                "response": str,
                "metadata": dict
            }
        """
        if self.backend_type == "local":
            return self._local_generate(prompt)
        else:
            return self._local_generate(prompt)

    def _local_generate(self, prompt: str) -> Dict[str, Any]:
        """
        A simple local response generator for demonstration purposes.
        """
        last_line = ""
        for line in prompt.strip().split("\n"):
            if line.startswith("User:"):
                last_line = line[5:].strip()

        response = self._template_response(last_line)

        return {
            "response": response,
            "metadata": {
                "backend": "local",
                "model": "template-v1",
            }
        }

    def _template_response(self, user_message: str) -> str:
        """
        Generates a simple template-based response.
        """
        lower = user_message.lower().strip()

        if not lower:
            return "I didn't catch that. Could you please rephrase your question?"

        greetings = ["hello", "hi", "hey", "good morning", "good evening", "howdy"]
        if any(lower.startswith(g) for g in greetings):
            return (
                "Hello! I'm Astra AI, your conversational assistant. "
                "How can I help you today?"
            )

        if "who are you" in lower or "what are you" in lower:
            return (
                "I'm Astra AI, a multipurpose conversational assistant designed "
                "to provide clear, accurate, and trustworthy information. "
                "I'm built on principles of transparency, safety, and trust."
            )

        if "help" in lower:
            return (
                "I can help with a variety of tasks including:\n"
                "- Answering general knowledge questions\n"
                "- Writing assistance and text editing\n"
                "- Reasoning and problem-solving\n"
                "- Explaining concepts clearly\n\n"
                "Just ask me anything!"
            )

        if "thank" in lower:
            return "You're welcome! Let me know if there's anything else I can help with."

        if lower in ["bye", "goodbye", "exit", "quit"]:
            return "Goodbye! It was nice chatting with you. Have a great day!"

        return (
            f"Thank you for your message. As Astra AI, I'm here to help. "
            f"While I'm currently running in demonstration mode with template responses, "
            f"I can still assist with basic conversations. "
            f"Feel free to ask me anything!"
        )
