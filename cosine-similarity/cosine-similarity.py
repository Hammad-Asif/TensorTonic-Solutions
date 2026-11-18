import numpy as np
import math
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    if not np.any(a) or not np.any(b):
        return 0.0
    return float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))