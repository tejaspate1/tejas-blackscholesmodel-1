"""
black_scholes_model.py

A simple implementation of the Black-Scholes option pricing model
for European call and put options.

Author: Your Name
License: MIT
"""

import numpy as np
from scipy.stats import norm


def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Price a European option using the Black-Scholes formula.

    Parameters:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate (annual, decimal form)
        sigma (float): Volatility of the underlying asset (annual, decimal form)
        option_type (str): "call" or "put"

    Returns:
        float: Option price
    """
    if T <= 0 or sigma <= 0 or S <= 0 or K <= 0:
        raise ValueError("Inputs must be positive and T, sigma > 0")

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type.lower() == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type.lower() == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price


if __name__ == "__main__":
    # Example: Option A (Low risk-free rate = 1%)
    S = 100     # stock price
    K = 100     # strike price
    T = 1.0     # 1 year to maturity
    r = 0.01    # 1% risk-free rate
    sigma = 0.20  # 20% volatility

    call_price = black_scholes(S, K, T, r, sigma, option_type="call")
    put_price = black_scholes(S, K, T, r, sigma, option_type="put")

    print("Example: Option A (Low Risk-Free Rate, r=1%)")
    print(f"Call Price: {call_price:.2f}")
    print(f"Put Price:  {put_price:.2f}")
