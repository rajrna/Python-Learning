from fuel import convert, gauge
import pytest

def test_int():
    assert convert("1/2") == 50

def test_char():
    with pytest.raises(ValueError):convert("a/b")

def test_negative_fract():
    with pytest.raises(ValueError):convert("-1/2")

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):convert("1/0")

def test_label_full():
    assert gauge(99) == "F"

def test_label_empty():
    assert gauge(1) == "E"

def test_normal():
    assert gauge(50) == "50%"
