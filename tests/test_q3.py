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
