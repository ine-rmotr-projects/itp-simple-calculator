from calculator import divide


def test_divide():
    results = divide(6, 2)
    assert results == 3


def test_divide_by_zero():
    results = divide(99, 0)
    assert type(results) == str
