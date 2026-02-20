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

The BackendAdapter decides what backend to use based on the configuration and then routes requests to the appropriate backend in either the local or cloud subfolder and does not handle the requests directly as it is just a router.
"""

import os
from typing import Dict, Any, List
from openai import OpenAI

config = "../../astra.config.json"

class BackendAdapter:
    """
    Provides a unified interface for generating model responses.
    Decides what backend to use based on the configuration.
    Routes to either the local or cloud subfolder based on the config set in the astra.config.json file.
    """
    def __init__(self, config: Dict[str, Any]):
        """
        Confirm that the config is valid and that the proper backend exists.
        """
        # config is stored in the astra.config.json file by default
        self.config = config
        # Initialize the appropriate backend based on the config
        if self.config["local_or_cloud"] == "local":
            self.backends = LocalBackend(self.config["local_model_config"])
            # Initialize the local model
        elif self.config["local_or_cloud"] == "cloud":
            self.backends = CloudBackend(self.config["cloud_model_config"])

