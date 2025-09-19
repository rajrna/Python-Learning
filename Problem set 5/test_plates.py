from plates import is_valid

def test_length():
    assert is_valid("HOLANUTET") == False

def test_begin_alpha():
    assert is_valid("12AB") == False
    assert is_valid("9HELLO") == False
    assert is_valid(".HELLO") == False

def test_begin_zero():
    assert is_valid("AA01") == False

def test_alpha_num():
    assert is_valid("HO//D0") == False
    assert is_valid("HELLO!") == False
    assert is_valid("AB CD") == False

def test_num_place():
    assert is_valid("HEL11A") == False
def test_without_beginning_alpha():
    assert is_valid("21xsas") == False
    assert is_valid("@sdfg") == False
    assert is_valid("22") == False
    assert is_valid("C5") == False

