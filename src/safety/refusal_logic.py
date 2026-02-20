"""
refusal_logic.py
---------
Refusal response generation for Astra AI.

This module handles:
- Generating consistent, professional refusal messages
- Mapping refusal reasons to user-friendly responses
- Offering constructive alternatives when possible
"""

from typing import Dict

REFUSAL_MESSAGES: Dict[str, str] = {
    "jailbreak_attempt": (
        "I'm unable to process that request. My safety guidelines and identity "
        "are fixed and cannot be altered through instructions, roleplay, or "
        "hypothetical framing. I'm happy to help with something else."
    ),
    "harmful_content": (
        "I'm not able to assist with that request, as it involves content that "
        "could lead to harm. If you have a different question or need help with "
        "something constructive, I'd be glad to help."
    ),
    "unsafe_content": (
        "I'm unable to assist with that type of request. I'm designed to provide "
        "safe, accurate, and helpful information. Let me know if there's something "
        "else I can help you with."
    ),
}

DEFAULT_REFUSAL = (
    "I'm sorry, but I can't help with that request. "
    "Please feel free to ask me something else."
)


class RefusalEngine:
    """
    Generates consistent refusal messages based on the type of safety violation.
    """

    def __init__(self):
        self.refusal_messages = REFUSAL_MESSAGES
        self.default_refusal = DEFAULT_REFUSAL

    def generate_refusal(self, reason: str = "unsafe_content") -> str:
        """
        Generates a refusal message for the given reason.

        Parameters:
            reason (str): The reason code from the safety filter.

        Returns:
            str: A user-friendly refusal message.
        """
        return self.refusal_messages.get(reason, self.default_refusal)
