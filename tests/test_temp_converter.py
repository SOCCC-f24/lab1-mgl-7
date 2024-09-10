import pytest
from temp_converter import f2c_op

def test_f2c_zero():
    assert round(f2c_op(0), 2) == -17.78  # Freezing point approximation

def test_f2c_five():
    assert round(f2c_op(5), 2) == -15.00

def test_f2c_negative_forty():
    assert round(f2c_op(-40), 2) == -40.00  # Fahrenheit and Celsius equal at -40
