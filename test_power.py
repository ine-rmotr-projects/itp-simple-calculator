from calculator import power


def test_power():
    results = power(2, 4)     #changing the value of power 
    assert results == 16

    results = power(2, 3)
    assert results == 8
