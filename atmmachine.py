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
        else:
            raise ValueError("Invalid transaction type processed.")

    def check_balance(self):
        return f"Current Balance: ₱{self.__balance:.2f}"

    def get_account_info(self):
        return f"--- Account Profile ---\nAccount #: {self.__account_number}\nAccount Name: {self.__account_name}\nCurrent Balance: ₱{self.__balance}"


print("--- ATM Activity 2 ---")

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

user_name = input("Enter your Account Name: ").strip()

atm = ATMMachine(user_number, user_name)

while True:
    print("="*30)
    print("\n--- ATM! ---")
    print("1. Deposit")
    print("2. Check Balance")
    print("3. Account Information")
    print("4. Exit")
    print("="*30)

    user_choice = input("\nChoose Option (1-4)").strip().lower()
    
    if user_choice in ['4', 'exit']:
        print("Thank you for using the ATM")
        break
        
    print("-" * 40)
    
    try:
        if user_choice == '1':
            amount = float(input("Enter deposit amount: ₱"))
            result = atm.process_transaction("deposit", amount)
            print(result)
            
        elif user_choice == '2':
            print(atm.check_balance())
            
        elif user_choice == '3':
            print(atm.get_account_info())
            
        else:
            print("Invalid Choice you dummy choose 1-4")
            
    except ValueError as error_message:
        print(f"ATM Rejected Action -> {error_message}")
        
    print("-" * 40)