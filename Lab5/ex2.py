class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance is {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest calculated: {interest}")
        self.balance += interest


class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_fee):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self.balance -= self.transaction_fee
        print(f"Deducted transaction fee. New balance is {self.balance}")


savings_account = SavingsAccount("SAV", 1000, 0.05)
savings_account.deposit(500)
savings_account.calculate_interest()
print()

checking_account = CheckingAccount("CHK", 2000, 5)
checking_account.withdraw(100)
checking_account.deduct_transaction_fee()
