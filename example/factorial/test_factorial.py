from factorial import *

def test_factorial():
    assert factorial(5) == 120

def test_logfactorial():
    assert factorial(5) == round(math.exp(logfactorial(5)))