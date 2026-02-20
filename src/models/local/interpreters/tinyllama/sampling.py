# sampling.py

def sample_next_token(logits: dict):
    """
    Picks the token with the highest score.
    """
    return max(logits, key=logits.get)