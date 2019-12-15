# Asercje


def div(a, b):
    return a/b

# Pod maską asercji
# if div(10, 5) == 2:
#     print("PASSED")
# else:
#     raise Exception("FAILED")
#
# if div(10, 2) == 5:
#     print("PASSED")
# else:
#     raise Exception("FAILED")


assert div(10, 5) == 2, "FAILED"
print("PASSED")
assert div(10, 2) == 5, "FAILED"
print("PASSED")


def kwa_sum(a, b):
    return (a+b)**2

assert kwa_sum(1, 1) == 4, "FAILED"
assert kwa_sum(0, 0) == 0, "FAILED"
assert kwa_sum(1.5, 1.5) == 9, "FAILED"


# Asercje nie służą tylko do testowania!
# def div(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero.")
#
# def div(a, b):
#     assert b!=0, "Nie można dzielić przez zero"
#     return a/b
#
# div(5,0)

def concatenate(str1, str2):
    return str1+str2

assert concatenate("asd", "fgh") == "asdfgh", "FAILED"
assert concatenate("qwe", "wq") == "qwewq", "FAILED"
assert concatenate("", "") == "", "FAILED"