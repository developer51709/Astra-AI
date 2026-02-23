import sys
import os
import json

# Ensure workspace is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_config():
    config_path = "astra.config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {}

def main():
    config = load_config()
    
    # Check if web interface is enabled
    if config.get("web_interface_enabled", False):
        print("[Astra] Starting Web Interface...")
        from src.web.app import run_web_server
        # Run web server in a way that doesn't block if possible, 
        # but for this script we'll just start it.
        run_web_server()
    else:
        print("[Astra] Starting CLI Interface...")
        from src.interface.cli import run_cli
        run_cli()

if __name__ == "__main__":
    main()
