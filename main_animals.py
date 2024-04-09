from animals import *
from bank_accounts import *

"""a = Animal()
c = Cat()
d = Dog()

a.make_sound()
c.make_sound()
d.make_sound()"""

b = BankAccount(100)
s = SavingsAccount(b, 50)

print(b)
print(s)

b.deposit(100)
s.deposit(200)

print(b)
print(s)

