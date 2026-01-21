"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q1 import validate_password

def test_validate_password_valid() -> None:
    assert validate_password("Abcdef1!") is True

def test_validate_password_invalid_prints_errors() -> None:
    assert validate_password("abc") is False

def test_validate_password_invalid_prints_error2() -> None:
    assert validate_password("123") is False