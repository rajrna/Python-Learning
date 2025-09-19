from twttr import shorten

def test_hello():
    assert shorten("hello")=="hll"

def test_upcase():
    assert shorten("HELLO")=="HLL"

def test_num():
    assert shorten("0123")=="0123"

def test_upprint():
    assert shorten("Hello")=="Hll"

def test_punct():
    assert shorten("hello.")=="hll."
