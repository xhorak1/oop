from .banking_account import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, bank_account, deposit=0):
        super().__init__(bank_account.withdraw(deposit) * 1.1)
        self.__bank_account = bank_account

    def deposit(self):
        self._balance += money * 1.1


