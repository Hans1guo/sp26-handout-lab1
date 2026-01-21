"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q2 import set_password

def test_set_password_valid_first_try() -> None:
    inputs = iter(["Abcdef1!"])
    set_password()


def test_set_password_invalid_then_valid() -> None:
    inputs = iter([
        "abc",       
        "Abcdef1!"    
    ])
    set_password()