"""Tests for Lab 1 Question 4"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q4 import most_common_letter

def test_most_common_letter_basic() -> None:
    assert most_common_letter("Hello") == "l"


def test_most_common_letter_ignore_case() -> None:
    assert most_common_letter("aAAbb") == "a"


def test_most_common_letter_no_letters() -> None:
    assert most_common_letter("123!!!") is None


def test_most_common_letter_tie_break() -> None:
    assert most_common_letter("bbAA") == "a"