class BankAccount:
    def __init__(
        self,
        account_number,
        account_name,
        account_type,
        initial_balance=0.0
    ):
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than ₱0.00!")

        self.balance += amount
        return f"Deposited ₱{amount:.2f}. New Balance: ₱{self.balance:.2f}."

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than ₱0.00!")
        if amount > self.balance:
            raise ValueError("Insufficient balance for this withdrawal.")

        self.balance -= amount
        return f"Withdrew ₱{amount:.2f}. New Balance: ₱{self.balance:.2f}."

    def check_balance(self):
        return f"Current Balance: ₱{self.balance:.2f}"

    def get_account_info(self):
        return (
            "--- Account Profile ---\n"
            f"Account #: {self.account_number}\n"
            f"Account Name: {self.account_name}\n"
            f"Account Type: {self.account_type}\n"
            f"Current Balance: ₱{self.balance:.2f}"
        )