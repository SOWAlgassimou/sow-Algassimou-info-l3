import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def correlation_test(x, y, rho0) :
    r = np.corrcoef(x, y)[0, 1]
    z = 0.5 * np.log((1 + r) / (1 – r))
    z0 = 0.5 * np.log((1 + rho0) / (1 – rho0))
    w = (z – z0) * np.sqrt(len(x) – 3)
    p_value = 2 * (1 – norm.cdf(abs(w)))
    return r, p_value
