"""
engine.py
---------
The Engine is the core processing unit of Astra AI. It is responsible for:

1. Assembling the final prompt (system prompt + conversation context + user message)
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

# These imports assume the corresponding modules exist.
from src.models.backend_adapter import BackendAdapter
from src.core.config import load_system_prompt


class Engine:
    """
    The Engine orchestrates the internal logic of Astra AI once a message
    has passed safety checks.

    Responsibilities:
    - Build the final prompt sent to the model
    - Maintain conversation state (short-term memory)
    - Call the backend adapter to generate a response
    - Format and return the model output
    """

    def __init__(self):
        # BackendAdapter abstracts the underlying LLM (local or API-based).
        self.backend = BackendAdapter()

        # Load the system prompt from the prompts directory.
        # This keeps the identity and behavior definition external and editable.
        self.system_prompt = load_system_prompt()

    # -------------------------------------------------------------------------
    # MAIN PROCESSING METHOD
    # -------------------------------------------------------------------------

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

        # ---------------------------------------------------------
        # 1. UPDATE CONVERSATION HISTORY
        # ---------------------------------------------------------
        # We store messages in a simple list structure:
        # [
        #   {"role": "user", "content": "..."},
        #   {"role": "assistant", "content": "..."}
        # ]
        history: List[Dict[str, str]] = conversation_state.get("history", [])
        history.append({"role": "user", "content": user_message})

        # ---------------------------------------------------------
        # 2. ASSEMBLE THE FINAL PROMPT
        # ---------------------------------------------------------
        # The prompt consists of:
        # - system prompt (identity + rules)
        # - conversation history
        # - the latest user message
        final_prompt = self._assemble_prompt(history)

        # ---------------------------------------------------------
        # 3. SEND PROMPT TO MODEL BACKEND
        # ---------------------------------------------------------
        # The backend adapter handles:
        # - formatting the request
        # - calling the model
        # - returning normalized output
        model_output = self.backend.generate(final_prompt)

        # ---------------------------------------------------------
        # 4. UPDATE STATE WITH ASSISTANT RESPONSE
        # ---------------------------------------------------------
        assistant_reply = model_output.get("response", "")
        history.append({"role": "assistant", "content": assistant_reply})

        updated_state = {"history": history}

        # ---------------------------------------------------------
        # 5. RETURN STRUCTURED OUTPUT
        # ---------------------------------------------------------
        return {
            "response": assistant_reply,
            "updated_state": updated_state
        }

    # -------------------------------------------------------------------------
    # INTERNAL HELPERS
    # -------------------------------------------------------------------------

    def _assemble_prompt(self, history: List[Dict[str, str]]) -> str:
        """
        Builds the final prompt string sent to the model.

        The structure is simple and readable:

        <SYSTEM PROMPT>

        Conversation:
        User: ...
        Assistant: ...
        User: ...

        Latest user message is already included in history.

        Returns:
            str: The full prompt text.
        """

        conversation_lines = []

        for message in history:
            role = message["role"].capitalize()
            content = message["content"]
            conversation_lines.append(f"{role}: {content}")

        conversation_block = "\n".join(conversation_lines)

        final_prompt = (
            f"{self.system_prompt}\n\n"
            "Conversation:\n"
            f"{conversation_block}\n"
        )

        return final_prompt
