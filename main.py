class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, initial_balance)
            return True
        return False

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return False

    def transfer(self, source_account_number, target_account_number, amount):
        if (source_account_number in self.accounts and
                target_account_number in self.accounts and
                self.accounts[source_account_number].withdraw(amount)):
            return self.accounts[target_account_number].deposit(amount)
        return False

    def get_account_summary(self):
        summary = {}
        for account_number, account in self.accounts.items():
            summary[account_number] = account.get_balance()
        return summary



if __name__ == "__main__":
    account_manager = AccountManager()
    account_manager.create_account("123")
    account_manager.create_account("456", 1000)
    account_manager.deposit("123", 500)
    account_manager.withdraw("456", 200)
    account_manager.transfer("456", "123", 100)
    print(account_manager.get_account_summary())

