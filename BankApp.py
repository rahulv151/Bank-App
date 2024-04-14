accounts = {}

def create_account(account_number):
    if account_number not in accounts:
        accounts[account_number] = 0
        print(f"\nAccount {account_number} created successfully.")
    else:
        print(f"\nAccount {account_number} already exists.")

def deposit(account_number, amount):
    if account_number in accounts and amount > 0:
        accounts[account_number] += amount
        print(f"\nDeposited Rs.{amount} into account {account_number}. New balance: Rs.{accounts[account_number]}")
    else:
        print("\nInvalid account or amount for deposit.")

def withdraw(account_number, amount):
    if account_number in accounts and amount > 0 and accounts[account_number] >= amount:
        accounts[account_number] -= amount
        print(f"\nWithdrew Rs.{amount} from account {account_number}. New balance: Rs.{accounts[account_number]}")
    else:
        print("\nInvalid account, amount, or insufficient balance for withdrawal.")

def check_balance(account_number):
    if account_number in accounts:
        print(f"\nAccount {account_number} balance: Rs.{accounts[account_number]}")
    else:
        print("\nAccount not found.")

while True:
    print("\nBank Application Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter account number: ")
        create_account(account_number)

    elif choice == '2':
        account_number = input("Enter account number: ")
        amount = float(input("Enter the deposit amount: Rs."))
        deposit(account_number, amount)

    elif choice == '3':
        account_number = input("Enter account number: ")
        amount = float(input("Enter the withdrawal amount: Rs."))
        withdraw(account_number, amount)

    elif choice == '4':
        account_number = input("Enter account number: ")
        check_balance(account_number)

    elif choice == '5':
        print("\nExiting the bank application. Have a nice day!")
        break

    else:
        print("\nInvalid choice. Please select a valid option.")
