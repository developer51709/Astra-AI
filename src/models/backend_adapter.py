"""
backend_adapter.py
---------
The BackendAdapter abstracts the underlying model implementation, allowing Astra AI to work with both local models and API-based services.

This module handles:
- Formatting requests for different backends
- Parsing responses from different backends
- Managing backend-specific configurations
- Providing a consistent interface to the Engine

This file is intentionally modular to allow easy addition of new backends.
"""

