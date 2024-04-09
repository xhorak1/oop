from animals import *
from bank_accounts import *
from calculator import Calculator

"""a = Animal()
c = Cat()
d = Dog()

a.make_sound()
c.make_sound()
d.make_sound()"""

"""b = BankAccount(100)
s = SavingsAccount(b, 50)

print(b)
print(s)

b.deposit(100)
s.deposit(200)

print(b.counter)
print(s.counter)

s.counter = 77
print(b.counter)
print(s.counter)"""


a = Calculator.add(3, 6)
print(a)

b = Calculator.ans_add(8)
c = Calculator.ans_add(4)
print(b)
print(c)

d = Calculator.multiple(5,5)
print(d)

e = Calculator.difference(8, 4)
print(e)

f = Calculator.minimum(8, 7, 5, 9)
print(f)

g = Calculator.maximum(4, 7, 9, 1)
print(g)

h = Calculator.average(8, 10, 6, 8)
print(h)

i = Calculator.factorial(5)
print(i)