# Create a class called `BankAccount` with attributes `account_number` and `balance`. Implement methods `deposit()` and `withdraw()` that update the account balance accordingly

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            return f"Deposited: Rs. {amount}. New balance: Rs. {self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdraw: Rs. {amount}. New balance: Rs. {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else: 
            return "Invalid withdrawal amount."