from calculator import subtract


def test_subtract():
    results = subtract(16, 6)  #changing the value of substract
    assert results == 10
