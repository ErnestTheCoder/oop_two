class ATMMachine:
    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = 0.00
        
    def process_transaction(self, action_type, amount=0.0):
        if action_type == "deposit":
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than ₱0.00!")
            self.__balance += amount
            return f"Deposited ₱{amount:.2f}. New Balance: ₱{self.__balance:.2f}."
        
        elif action_type == "withdraw":
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than ₱0.00!")
            if amount > self.__balance:
                raise ValueError("Insufficient balance for this withdrawal.")
            self.__balance -= amount
            return f"Withdrew ₱{amount:.2f}. New Balance: ₱{self.__balance:.2f}."
        
        else:
            raise ValueError("Invalid transaction type processed.")

    def check_balance(self):
        return f"Current Balance: ₱{self.__balance:.2f}"

    def get_account_info(self):
        return f"--- Account Profile ---\nAccount #: {self.__account_number}\nAccount Name: {self.__account_name}\nCurrent Balance: ₱{self.__balance:.2f}"


print("--- ATM Activity 3 ---")

while True:
    user_input = input("Enter your Account Number: ").strip()
    if user_input == "":
        print("Input cannot be empty. Please try again.")
        continue
    try:
        user_number = float(user_input)
        break
    except ValueError:
        print("Invalid Account Number. Please enter numbers only.")

while True:
    user_name = input("Enter your Account Name: ").strip()
    if user_name == "":
        print("Input cannot be empty. Please try again.")
        continue
    if not all(c.isalpha() or c.isspace() for c in user_name):
        print("Invalid Account Name. Please enter letters only.")
        continue
    break

atm = ATMMachine(user_number, user_name)

while True:
    print("\n" + "="*30)
    print("--- ATM! ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Information")
    print("5. Exit")
    print("="*30)

    user_choice = input("\nChoose Option (1-5): ").strip().lower()
    
    if user_choice in ['5', 'exit']:
        print("Thank you for using the ATM")
        break
        
    print("-" * 40)
    
    try:
        if user_choice == '1':
            amount = float(input("Enter deposit amount: ₱"))
            result = atm.process_transaction("deposit", amount)
            print(result)
            
        elif user_choice == '2':
            amount = float(input("Enter withdrawal amount: ₱"))
            result = atm.process_transaction("withdraw", amount)
            print(result)
            
        elif user_choice == '3':
            print(atm.check_balance())
            
        elif user_choice == '4':
            print(atm.get_account_info())
            
        else:
            print("Invalid Choice. Please choose between 1 and 5.")
            
    except ValueError as error_message:
        print(f"ATM Rejected Action -> {error_message}")
        
    print("-" * 40)