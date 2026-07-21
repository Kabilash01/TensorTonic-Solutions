import math

def elu(x, alpha=1.0):
    """
    Apply ELU activation to each element.
    """
    return [v if v > 0 else alpha * (math.exp(v) - 1) for v in x]
