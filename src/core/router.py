"""
router.py
---------
The Router is responsible for directing incoming user messages through the
correct processing pipeline inside Astra AI. It acts as the "traffic controller"
between the interface layer (CLI/API), the safety layer, the core engine, and
the model backend.

This file is intentionally simple and modular so it can grow as Astra AI evolves.
"""

from typing import Dict, Any

# These imports assume the corresponding modules exist.
# They can be implemented later as the project grows.
from src.safety.filters import SafetyFilter
from src.safety.refusal_logic import RefusalEngine
from src.core.engine import Engine


class Router:
    """
    The Router coordinates the flow of a single user request.

    Responsibilities:
    - Receive a message from the interface layer
    - Run the message through safety filters
    - Forward safe messages to the core engine
    - Handle refusals for unsafe messages
    - Return a structured response back to the interface layer

    The Router does NOT:
    - Perform safety checks itself
    - Generate model responses directly
    - Store long-term conversation state
    """

    def __init__(self):
        # SafetyFilter handles detection of harmful or disallowed content.
        self.safety_filter = SafetyFilter()

        # RefusalEngine generates consistent refusal messages.
        self.refusal_engine = RefusalEngine()

        # Engine handles prompt assembly, backend communication, and response formatting.
        self.engine = Engine()

    def handle_request(self, user_message: str, conversation_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main entry point for processing a user message.

        Parameters:
            user_message (str): The raw text input from the user.
            conversation_state (dict): A dictionary containing conversation history
                                       and any temporary state needed by the engine.

        Returns:
            dict: A structured response containing:
                - "response": The assistant's reply text
                - "safe": Whether the message passed safety checks
                - "refused": Whether the request was refused
                - "updated_state": Updated conversation state
        """

        # ---------------------------------------------------------
        # 1. SAFETY CHECK
        # ---------------------------------------------------------
        # The safety filter analyzes the user message for harmful intent,
        # disallowed content, or jailbreak attempts.
        safety_result = self.safety_filter.evaluate(user_message)

        if not safety_result["allowed"]:
            # If the message is unsafe, we do NOT pass it to the engine.
            # Instead, we generate a refusal response.
            refusal_text = self.refusal_engine.generate_refusal(
                reason=safety_result.get("reason", "unsafe_content")
            )

            return {
                "response": refusal_text,
                "safe": False,
                "refused": True,
                "updated_state": conversation_state  # State does not change on refusal
            }

        # ---------------------------------------------------------
        # 2. SAFE REQUEST → FORWARD TO ENGINE
        # ---------------------------------------------------------
        # The engine handles:
        # - prompt assembly
        # - backend communication
        # - formatting the final response
        engine_output = self.engine.process(
            user_message=user_message,
            conversation_state=conversation_state
        )

        # The engine returns both the assistant's reply and updated state.
        return {
            "response": engine_output["response"],
            "safe": True,
            "refused": False,
            "updated_state": engine_output["updated_state"]
        }


# ---------------------------------------------------------
# OPTIONAL: Convenience function for external callers
# ---------------------------------------------------------

def route_message(user_message: str, conversation_state: Dict[str, Any]) -> Dict[str, Any]:
    """
    A simple wrapper for environments that prefer functional-style access
    instead of instantiating Router manually.

    Example usage (CLI or API layer):
        result = route_message("Hello Astra!", state)
        print(result["response"])
    """
    router = Router()
    return router.handle_request(user_message, conversation_state)
