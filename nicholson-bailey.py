import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def nicholson_bailey_model(generations=30, beta=2, alpha=0.05, g=1, H0=20, P0=2) :
    H, P = [H0], [P0]
    for _ in range(generations) :
        H_next = beta * H[-1] * np.exp(-alpha * P[-1])
        P_next = g * H[-1] * (1 – np.exp(-alpha * P[-1]))
        H.append(H_next)
        P.append(P_next)
    return H, P
