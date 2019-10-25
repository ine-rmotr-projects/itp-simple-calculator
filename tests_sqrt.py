from calculator import sqrt

def test_sqrt():
    results = sqrt(16)
    assert results == 4 #changing the value of sqrt

    results = sqrt(25)
    assert results == 5

