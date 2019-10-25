from calculator import multiply


def test_multiply():
    results = multiply(4, 2)   #changing the value of multiply
    assert results == 8
