import hashlib
import math
import re


VECTOR_DIMENSIONS = 1536


def tokenize_text(text):
    print("[EMBED-1] Tokenizing text...")

    if text is None:
        return []

    text = text.lower()
    tokens = re.findall(r"[a-zA-Z0-9_]+", text)

    print(f"[EMBED-2] Found {len(tokens)} tokens.")
    return tokens


def create_local_embedding(text):

    """
    Creates a local 1536-dimensional embedding vector from input text.
    This vector represents the text numerically so SQL Server can compare it
    against stored knowledge base embeddings using vector search.
    """
    print("[EMBED-3] Creating local embedding vector...")

    tokens = tokenize_text(text)
    """
    Splits input text into normalized lowercase tokens.
    These tokens are later used to build the local embedding vector.
    """
    vector = [0.0] * VECTOR_DIMENSIONS

    for token in tokens:
        hash_value = hashlib.sha256(token.encode("utf-8")).hexdigest()

        index = int(hash_value[:8], 16) % VECTOR_DIMENSIONS
        sign = 1.0 if int(hash_value[8:10], 16) % 2 == 0 else -1.0

        vector[index] += sign

    print("[EMBED-4] Raw vector created.")

    length = math.sqrt(sum(value * value for value in vector))

    if length > 0:
        vector = [value / length for value in vector]
        print("[EMBED-5] Vector normalized successfully.")
    else:
        print("[EMBED-5] Empty text received. Returning zero vector.")

    print(f"[EMBED-6] Vector size: {len(vector)}")
    return vector