import unittest


class MyCalculator():
    def factorial(a):
        if not isinstance(a, int):
            return 0
        if a < 0:
            return 0
        if a == 0:
            return 1
        output = 1
        for i in range(1, a + 1):
            output *= i
        return output

    def plus(a, b):
        if not isinstance(a, int):
            return 0
        if not isinstance(b, int):
            return 0
        return a + b


a = MyCalculator.factorial(5)

print(a)
