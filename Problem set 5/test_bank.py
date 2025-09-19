from bank import value
import pytest

def test_hello():
    assert value("hello") == 0
def test_start_w_h():
    assert value("hey") == 20
def test_other():
    assert value("abra ca dabra")== 100
def test_upcase():
    assert value("HELLO")==0
