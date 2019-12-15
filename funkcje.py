def add(x, y):
    return x+y


def product(x, y):
    return x*y


def is_palindrom(str1):
    return str1.lower().replace(" ", "") == str1[::-1].lower().replace(" ", "")