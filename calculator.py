class Calculator:
    ans = 0
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def divide(a, b):
        return a / b

    @classmethod
    def ans_add(cls, a):
        cls.ans += a
        return cls.ans

    @classmethod
    def clean_ans(cls):
        cls.ans = 0

    @staticmethod
    def multiple(a, b):
        return a * b

    @staticmethod
    def difference(a, b):
        return a - b

    @staticmethod
    def minimum(a,b,c,d):
        return min(a,b,c,d)

    @staticmethod
    def maximum(a,b,c,d):
        return max(a,b,c,d)
    @staticmethod
    def average(a,b,c,d):
        return (a+b+c+d)/4

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

