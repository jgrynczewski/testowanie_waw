import math

def add(x, y):
    return x+y


def product(x, y):
    return x*y


def is_palindrom(str1):
    return str1.lower().replace(" ", "") == str1[::-1].lower().replace(" ", "")


def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    if type(r) not in [int, float]:
        raise TypeError("The radius be a non-negative real number.")

    return math.pi * r**2