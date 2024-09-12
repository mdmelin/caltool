import matplotlib
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

tcolor = dict(r = lambda s: f'\033[91m{s}\033[0m',
              g = lambda s: f'\033[92m{s}\033[0m',
              y = lambda s: f'\033[93m{s}\033[0m',
              b = lambda s: f'\033[94m{s}\033[0m',
              m = lambda s: f'\033[95m{s}\033[0m',
              c = lambda s: f'\033[96m{s}\033[0m',
              )

def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def cubic(x, a, b, c, d):
    return a * x**2 + b * x + c

def inverse_from_coefficients(coefs, y):
    """
    For a polynomial with coefficients coefs, find the roots at y.
    This is useful for finding the inverse of a calibration curve (ie. the input value that will achieve the deired output value).
    """
    polyfunc = np.poly1d(coefs)
    roots = (polyfunc - y).r
    return roots

def sanitize_roots(roots, input_values):
    """
    Given a list of roots, return only real roots 
    that are close in value to the calibration curve.
    """
    
    # remove complex roots
    roots = roots[np.isreal(roots)].real
    
    # Filter out roots that are not close to the calibration curve values
    min = np.mean(input_values) - 3*np.std(input_values)
    max = np.mean(input_values) + 3*np.std(input_values)
    roots = roots[(roots > min) & (roots < max)]

    assert len(roots) == 1, f'Expected 1 root, got {len(roots)}. Check your curve or the value you are requesting.'
    return roots[0]

    
