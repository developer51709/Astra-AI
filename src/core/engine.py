"""
engine.py
---------
The Engine is the core processing unit of Astra AI. It is responsible for:

1. Assembling the conversation messages (system prompt + history)
2. Communicating with the model backend
3. Formatting and returning the model's response
4. Managing short-term conversation state

The Engine does NOT:
- Perform safety checks (handled by the safety layer)
- Route requests (handled by router.py)
- Implement backend logic directly (handled by backend adapters)

This file is intentionally modular and easy to extend as Astra AI evolves.
"""

from typing import Dict, Any, List

from src.models.backend_adapter import BackendAdapter
from src.core.config import load_system_prompt


class Engine:
    """
    The Engine orchestrates the internal logic of Astra AI once a message
    has passed safety checks.

    Responsibilities:
    - Build the message list sent to the model
    - Maintain conversation state (short-term memory)
    - Call the backend adapter to generate a response
    - Format and return the model output
    """

    def __init__(self):
        self.backend = BackendAdapter()
        self.system_prompt = load_system_prompt()

    def process(self, user_message: str, conversation_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes a user message after it has passed safety checks.

        Parameters:
            user_message (str): The user's input text.
            conversation_state (dict): Contains conversation history and metadata.

        Returns:
            dict: {
                "response": str,
                "updated_state": dict
            }
        """
        history: List[Dict[str, str]] = conversation_state.get("history", [])
        history.append({"role": "user", "content": user_message})

        model_output = self.backend.generate(self.system_prompt, history)

        assistant_reply = model_output.get("response", "")
        history.append({"role": "assistant", "content": assistant_reply})

        updated_state = {"history": history}

        return {
            "response": assistant_reply,
            "updated_state": updated_state
        }
