# test_example.py
import pytest

# Function to test
def add(a, b):
    return a + b

# Test case for add function
def test_add():
    assert add(2, 3) == 5  # Test that 2 + 3 equals 5

def test_add_negative():
    assert add(-1, 1) == 0  # Test that -1 + 1 equals 0

def test_add_zero():
    assert add(0, 0) == 0  # Test that 0 + 0 equals 0
