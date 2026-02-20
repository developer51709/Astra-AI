# forward.py
import random

def forward_pass(tokens):
    """
    Placeholder forward pass.
    Returns a fake logits dict.
    """
    vocab = ["hello", "world", "tiny", "llama", "test", "response"]
    logits = {word: random.random() for word in vocab}
    return logits