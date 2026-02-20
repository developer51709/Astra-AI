"""
utils.py
---------
Utility functions for Astra AI interface layer.

This module provides helper functions used across the interface components.
"""


def truncate_text(text: str, max_length: int = 500) -> str:
    """Truncates text to a maximum length with an ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def format_response(response: str, prefix: str = "Astra AI") -> str:
    """Formats a response with the assistant prefix."""
    return f"{prefix}: {response}"
