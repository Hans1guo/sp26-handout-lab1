"""Tests for Lab 1 Question 3"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q3 import (
    income_tax_fed,
    income_tax_ca,
    income_tax_ma,
    income_tax_ny,
    calculate_income_tax
)

def test_income_tax_zero_income() -> None:
    assert income_tax_fed(0) == 0.0
    assert income_tax_ca(0) == 0.0
    assert income_tax_ma(0) == 0.0
    assert income_tax_ny(0) == 0.0


def test_income_tax_positive() -> None:
    assert income_tax_fed(10000) > 0
    assert income_tax_ca(10000) > 0
    assert income_tax_ma(10000) == 500.0
    assert income_tax_ny(10000) > 0


def test_income_tax_monotonic() -> None:
    assert income_tax_fed(20000) >= income_tax_fed(10000)
    assert income_tax_ca(20000) >= income_tax_ca(10000)
    assert income_tax_ny(20000) >= income_tax_ny(10000)