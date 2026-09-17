from calculator import add

def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(6, 0) == 6


def test_add_negative():
    assert add(-5, 1) == -4