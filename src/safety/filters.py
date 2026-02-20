"""
filters.py
---------
Safety filter for Astra AI.

This module handles:
- Detecting harmful or disallowed content in user messages
- Checking for jailbreak attempts
- Returning structured safety evaluation results
"""

from typing import Dict, Any, List

BLOCKED_PATTERNS: List[str] = [
    "ignore your instructions",
    "ignore all previous",
    "disregard your rules",
    "pretend you are",
    "act as if you have no restrictions",
    "bypass your safety",
    "override your programming",
    "forget your instructions",
    "you are now",
    "new instructions:",
]

HARMFUL_KEYWORDS: List[str] = [
    "how to make a bomb",
    "how to hack",
    "how to steal",
    "how to hurt",
    "how to kill",
]


class SafetyFilter:
    """
    Evaluates user messages for safety violations.

    The filter checks for:
    - Known jailbreak patterns
    - Harmful content keywords
    - Prompt injection attempts
    """

    def __init__(self):
        self.blocked_patterns = BLOCKED_PATTERNS
        self.harmful_keywords = HARMFUL_KEYWORDS

    def evaluate(self, message: str) -> Dict[str, Any]:
        """
        Evaluates a user message for safety.

        Parameters:
            message (str): The user's input text.

        Returns:
            dict: {
                "allowed": bool,
                "reason": str or None
            }
        """
        lower_message = message.lower().strip()

        for pattern in self.blocked_patterns:
            if pattern in lower_message:
                return {
                    "allowed": False,
                    "reason": "jailbreak_attempt",
                }

        for keyword in self.harmful_keywords:
            if keyword in lower_message:
                return {
                    "allowed": False,
                    "reason": "harmful_content",
                }

        return {
            "allowed": True,
            "reason": None,
        }
