from calculator import sqrt

def test_sqrt():
    results = sqrt(9)
    assert results == 3

    results = sqrt(16)
    assert results == 4

