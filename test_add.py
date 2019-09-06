from calculator import add


def test_add():
    results = add(1, 2)
    assert results == 3
