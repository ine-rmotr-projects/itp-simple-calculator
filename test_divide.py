from calculator import divide


def test_divide():
    results = divide(12, 3)  #changing the value of divide
    assert results == 4


def test_divide_by_zero():
    results = divide(99, 0)
    assert type(results) == str
