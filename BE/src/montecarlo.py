# https://ipythonquant.wordpress.com/2018/05/22/tensorflow-meets-quantitative-finance-pricing-exotic-options-with-monte-carlo-simulations-in-tensorflow/

import numpy as np
import scipy.stats as stats


def black_scholes(S, K, dt, sigma, r):
    """
    Black-Scholes algorithm
    :param S: Initial price
    :param K: Strike
    :param dt: Time to Expiry - Delta of Time
    :param sigma: Implied Vol
    :param r: Risk Free Rate
    Adapted from https://ipythonquant.wordpress.com/2018/05/22/tensorflow-meets-quantitative-finance-pricing-exotic-options-with-monte-carlo-simulations-in-tensorflow/
    :return:
    """
    Phi = stats.norm.cdf
    d_1 = (np.log(S / K) + (r + sigma ** 2 / 2) * dt) / (sigma * np.sqrt(dt))
    d_2 = d_1 - sigma * np.sqrt(dt)
    return S * Phi(d_1) - K * np.exp(-r * dt) * Phi(d_2)


def monte_carlo(S0, K, T, sigma, r, q=0, nr_of_steps=50, nr_of_paths=100):
    S = []
    dt = T / nr_of_steps
    for path in range(0, nr_of_paths):
        S_ = [{"val": S0, "step": 0}]
        for step in range(1, nr_of_steps):
            e = np.random.normal()
            val = S_[-1]["val"] * np.exp(((r - q - (sigma ** 2 / 2)) * dt) + (sigma * e * np.sqrt(dt)))
            S_.append({"val": val, "step": step})
        S.append(S_)
    return S
