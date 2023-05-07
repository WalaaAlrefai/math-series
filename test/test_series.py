import pytest
from math_series.series import fibonacci
from math_series.series import lucas

def test_fib_minus_equals_string():
     assert fibonacci(-1) == "Incorrect input"

def test_fib_0_equals_0():
     assert fibonacci(0) == 0

def test_fib_1_equals_1():
     assert fibonacci(1) == 1

def test_fib_2_equals_1():
     assert fibonacci(2) == 1

def test_fib_6_equals_8():
    assert fibonacci(6) == 8

def test_lucas_one():
     assert lucas(1) == 1

def test_lucas_zero():
     assert lucas(0) == 2

def test_lucas_nine():
     assert lucas(9) == 76

def test_lucas_string():
     assert lucas(-1) == "Incorrect input"