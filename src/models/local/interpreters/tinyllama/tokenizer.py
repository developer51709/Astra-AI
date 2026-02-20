# tokenizer.py

class TinyTokenizer:
    """
    Placeholder tokenizer.
    Real implementation will load vocab from GGUF metadata.
    """

    def encode(self, text: str):
        # Fake tokenization: split by spaces
        return text.split()

    def decode(self, tokens):
        return " ".join(tokens)