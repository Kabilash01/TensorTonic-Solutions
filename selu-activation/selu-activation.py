import math

def selu(x):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    lam = 1.05070
    alpha = 1.6733
    result = []
    for val in x:
        if val > 0:
            result.append(round(lam * val, 4))
        else:
            result.append(round(lam * alpha * (math.exp(val) - 1), 4))
    return result
