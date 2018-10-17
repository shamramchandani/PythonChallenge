from app.calculator import Calculator
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_add_simple_int(calculator):
    assert(calculator.add(1,1) == 2)

def test_add_simple_float(calculator):
    assert(calculator.add(1.6,1.5) == 3.1)

# def test_add_long_float(calculator):
#     assert(calculator.add(1.52435,9.5776876) == 11.1020376)

def test_subtract_simple_int(calculator):
    assert(calculator.subtract(1,1) == 0)

def test_subtract_simple_float(calculator):
    assert(calculator.add(3.5,1) == 2.5)

def test_add_simple_int(calculator):
    assert(calculator.add(1,1) == 2)

def test_add_simple_float(calculator):
    assert(calculator.add(1.6,1.5) == 3.1)

def test_add_simple_int(calculator):
    assert(calculator.add(1,1) == 2)

def test_add_simple_float(calculator):
    assert(calculator.add(1.6,1.5) == 3.1)