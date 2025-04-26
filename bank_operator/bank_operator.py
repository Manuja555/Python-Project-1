from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users created yet.\n")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:
        print("Error: No users available. You must create a user before adding an account.\n")
        return

    list_users()
    while True:
        try:
            idx = int(input("Select user number: ")) - 1
            if 0 <= idx < len(users):
                break
            else:
                print("Invalid user number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    while True:
        try:
            account_choice = int(input("Enter your choice (1, 2, 3): "))
            if account_choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            amount = float(input("Enter initial deposit: "))
            if amount >= 0:
                break
            else:
                print("Initial deposit must be a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added to {users[idx].name}!\n")

def deposit_money():
    if not users:
        print("Error: No users available. Please create a user first.\n")
        return

    list_users()
    while True:
        try:
            user_idx = int(input("Select user number: ")) - 1
            if 0 <= user_idx < len(users):
                user = users[user_idx]
                break
            else:
                print("Invalid user number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not user.accounts:
        print(f"{user.name} has no accounts yet.\n")
        return

    print(f"\n{user.name}'s Accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")

    while True:
        try:
            acc_idx = int(input("Select account number: ")) - 1
            if 0 <= acc_idx < len(user.accounts):
                break
            else:
                print("Invalid account number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                user.accounts[acc_idx].deposit(amount)
                print("Deposit successful.\n")
                break
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def withdraw_money():
    if not users:
        print("Error: No users available. Please create a user first.\n")
        return

    list_users()
    while True:
        try:
            user_idx = int(input("Select user number: ")) - 1
            if 0 <= user_idx < len(users):
                user = users[user_idx]
                break
            else:
                print("Invalid user number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not user.accounts:
        print(f"{user.name} has no accounts yet.\n")
        return

    print(f"\n{user.name}'s Accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")

    while True:
        try:
            acc_idx = int(input("Select account number: ")) - 1
            if 0 <= acc_idx < len(user.accounts):
                break
            else:
                print("Invalid account number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                try:
                    user.accounts[acc_idx].withdraw(amount)
                    print("Withdrawal successful.\n")
                    break
                except ValueError as e:
                    print(f"Error: {e}\n")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_transactions():
    if not users:
        print("Error: No users available. Please create a user first.\n")
        return

    list_users()
    while True:
        try:
            user_idx = int(input("Select user number: ")) - 1
            if 0 <= user_idx < len(users):
                user = users[user_idx]
                break
            else:
                print("Invalid user number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not user.accounts:
        print(f"{user.name} has no accounts yet.\n")
        return

    print(f"\n{user.name}'s Accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"\n{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
        print("Transaction History:")
        for tx in acc.get_transaction_history():
            print(f"- {tx}")
        if not acc.get_transaction_history():
            print("No transactions yet.")