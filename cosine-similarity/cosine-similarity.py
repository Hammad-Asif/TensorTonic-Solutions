import numpy as np
import math
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a=np.asarray(a,dtype=float)
    b=np.asarray(b,dtype=float)
    if not np.any(a) or not np.any(b):
        return 0.0
    prod=np.dot(a,b)
    normA=np.linalg.norm(a)
    normB=np.linalg.norm(b)
    return float(prod/(normA*normB))