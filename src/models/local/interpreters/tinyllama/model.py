# model.py
from .gguf_reader import GGUFReader
from .tokenizer import TinyTokenizer
from .forward import forward_pass
from .sampling import sample_next_token

class TinyLlamaModel:
    """
    Minimal functional TinyLlama interpreter.
    """

    def __init__(self, config):
        self.config = config
        self.reader = GGUFReader(config["model_path"])
        self.tokenizer = TinyTokenizer()

    def generate(self, system_prompt, history):
        # Build prompt
        prompt = system_prompt + "\n"
        for msg in history:
            prompt += f"{msg['role']}: {msg['content']}\n"

        tokens = self.tokenizer.encode(prompt)

        # Generate 20 tokens max
        for _ in range(20):
            logits = forward_pass(tokens)
            next_token = sample_next_token(logits)
            tokens.append(next_token)

        return {
            "response": self.tokenizer.decode(tokens),
            "metadata": {
                "backend": "tinyllama",
                "mode": "placeholder"
            }
        }