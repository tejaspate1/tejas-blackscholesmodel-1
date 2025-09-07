"""
test_black_scholes.py

Unit tests for the black_scholes_model.py implementation.
Run with: pytest tests/
"""

import pytest
from black_scholes_model import black_scholes


def test_call_option_low_rate():
    S, K, T, r, sigma = 100, 100, 1.0, 0.01, 0.20
    price = black_scholes(S, K, T, r, sigma, option_type="call")
    assert round(price, 2) == 8.43


def test_put_option_low_rate():
    S, K, T, r, sigma = 100, 100, 1.0, 0.01, 0.20
    price = black_scholes(S, K, T, r, sigma, option_type="put")
    assert round(price, 2) == 7.43


def test_invalid_option_type():
    with pytest.raises(ValueError):
        black_scholes(100, 100, 1, 0.01, 0.20, option_type="invalid")


def test_invalid_inputs():
    with pytest.raises(ValueError):
        black_scholes(-100, 100, 1, 0.01, 0.20, option_type="call")
