"""
cli.py
---------
Command-line interface for Astra AI.

This module handles:
- Providing a user-friendly CLI for interacting with Astra AI
- Parsing command-line arguments
- Displaying formatted output

The CLI is designed to be simple and intuitive, making Astra AI accessible
and useful for both developers and end-users.
"""

import sys
from src.core.router import Router


def print_banner():
    """Prints the Astra AI welcome banner."""
    print()
    print("=" * 50)
    print("       ✦ Astra AI — Conversational Assistant")
    print("=" * 50)
    print()
    print("  Type your message and press Enter to chat.")
    print("  Type 'exit' or 'quit' to end the session.")
    print()


def run_cli():
    """
    Main entry point for the Astra AI CLI.

    Starts an interactive conversation loop where the user can
    chat with Astra AI in the terminal.
    """
    print_banner()

    router = Router()
    conversation_state = {"history": []}

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye! Have a great day!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("\nAstra AI: Goodbye! It was nice chatting with you. Have a great day!\n")
            break

        result = router.handle_request(user_input, conversation_state)

        conversation_state = result["updated_state"]

        if result.get("refused"):
            print(f"\nAstra AI [Safety]: {result['response']}\n")
        else:
            print(f"\nAstra AI: {result['response']}\n")


if __name__ == "__main__":
    run_cli()
