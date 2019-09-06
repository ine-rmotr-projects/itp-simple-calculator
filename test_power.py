from calculator import power


def test_power():
    results = power(3, 2)
    assert results == 9

    results = power(3, 3)
    assert results == 27