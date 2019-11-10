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
    d_1 = (np.log(S / K) + (r+sigma**2/2)*dt) / (sigma*np.sqrt(dt))
    d_2 = d_1 - sigma*np.sqrt(dt)
    return S*Phi(d_1) - K*np.exp(-r*dt)*Phi(d_2)