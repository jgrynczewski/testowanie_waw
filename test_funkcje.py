import funkcje


def test_add():
    assert funkcje.add(7, 3) == 10
    assert funkcje.add(7, -1) == 6
    assert funkcje.add(4.3, 5.3) == 9.6


def test_product():
    assert funkcje.product(5, 5) == 25
    assert funkcje.product(5, 2.5) == 12.5
    assert funkcje.product(0, 0) == 0


def test_is_palindrom():
    assert funkcje.is_palindrom("adsa")
    assert funkcje.is_palindrom("")
    assert funkcje.is_palindrom("Kobyła ma Mały Bok")


test_add()
test_product()
test_is_palindrom()