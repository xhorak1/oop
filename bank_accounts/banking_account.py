class BankAccount:
    counter = 0

    def __init__(self, deposit=0):
        self._balance = deposit
    def deposit(self, money):
        self._balance += money

    def add_counter(cls, num):
        cls.counter += num

    def withdraw(self, money):
        try:
            if self._balance >= money:
                self._balance -= money
                return money
        except:
            raise ValueError


    def __str__(self):
        return f"na uctu je: {self._balance} penez"

