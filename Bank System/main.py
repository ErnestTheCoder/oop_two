from bank_account import BankAccount


def main():
    while True:
        account_number = input("Enter your Account Number: ").strip()

        if not account_number:
            print("Input cannot be empty. Please try again.")
            continue

        if not account_number.isdigit():
            print("Invalid Account Number. Please enter numbers only.")
            continue

        break

    while True:
        account_name = input("Enter your Account Name: ").strip()

        if not account_name:
            print("Input cannot be empty. Please try again.")
            continue

        if not all(char.isalpha() or char.isspace() for char in account_name):
            print("Invalid Account Name. Please enter letters only.")
            continue

        break

    while True:
        account_type = input("Enter your Account Type: ").strip()

        if not account_type:
            print("Input cannot be empty. Please try again.")
            continue

        if not all(char.isalpha() or char.isspace() for char in account_type):
            print("Invalid Account Type. Please enter letters only.")
            continue

        break

    while True:
        initial_balance = input("Enter Initial Balance: ₱").strip()

        if not initial_balance:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            initial_balance = float(initial_balance)

            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                continue

            break
        except ValueError:
            print("Invalid balance. Please enter a valid number.")

    account = BankAccount(
        account_number=account_number,
        account_name=account_name,
        account_type=account_type,
        initial_balance=initial_balance
    )

    while True:
        print("\n===== BANK ACCOUNT =====")
        print("1. Display Account Information")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                print(account.get_account_info())
            elif choice == "2":
                amount = float(input("Enter deposit amount: ₱"))
                print(account.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: ₱"))
                print(account.withdraw(amount))
            elif choice == "4":
                print(account.check_balance())
            elif choice == "5":
                print("Thank you for using the bank system by Ernest Jhun F. Telano.")
                break
            else:
                print("Invalid option.")

        except ValueError as error:
            print(f"Transaction failed: {error}")


if __name__ == "__main__":
    main()
