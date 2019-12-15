def add(x, y):
    return x+y

def product(x, y):
    return x*y

def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5.3) == 9.6

def test_product():
    assert product(5, 5) == 25
    assert product(5, 2.5) == 12.5
    assert product(0, 0) == 0
