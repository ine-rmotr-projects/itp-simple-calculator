from calculator import square


def test_square():
    results = square(4)   #changing the value of square
    assert results == 16
