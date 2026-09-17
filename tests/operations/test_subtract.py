from calculator import subtract

def test_subtract():
    assert subtract(4, 2) == 2


def test_subtract_negative():
    assert subtract(3, 7) == -4


def test_subtract_zero():
    assert subtract(5, 0) == 5