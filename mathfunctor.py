
class MathFunctor:

    def __init__(self, operation):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == "+":
            return a + b

        if self.operation == "-":
            return a - b

        if self.operation == "*":
            return a * b

        if self.operation == "/":
            return a / b


součet = MathFunctor("+")
print(součet(5,6))
rozdíl = MathFunctor("-")
print(rozdíl(5,6))
součin = MathFunctor("*")
print(součin(5,6))
podíl = MathFunctor("/")
print(podíl(5,6))