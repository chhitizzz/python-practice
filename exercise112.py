# Create a class called `BankAccount` with attributes `account_number` and `balance`. Implement methods `deposit()` and `withdraw()` that update the account balance accordingly

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance