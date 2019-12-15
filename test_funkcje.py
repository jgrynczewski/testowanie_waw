import funkcje
import pytest


def test_add():
    assert funkcje.add(7, 3) == 10
    assert funkcje.add(7, -1) == 6
    assert funkcje.add(4.3, 5.3) == 9.6


def test_product():
    assert funkcje.product(5, 5) == 25
    assert funkcje.product(5, 2.5) == 12.5
    assert funkcje.product(0, 0) == 0


def test_is_palindrom():
    assert funkcje.is_palindrom("asdsa")
    assert funkcje.is_palindrom("")
    assert funkcje.is_palindrom("Kobyła ma Mały Bok")

def test_area():
    assert funkcje.circle_area(1) == funkcje.math.pi
    assert funkcje.circle_area(0) == 0
    assert funkcje.circle_area(2.1) == funkcje.math.pi* (2.1**2)

def test_values():
    with pytest.raises(ValueError):
        funkcje.circle_area(-2)

def test_type():
    with pytest.raises(TypeError):
        funkcje.circle_area("asd")