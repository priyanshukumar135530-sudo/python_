balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited:", amount)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Amount Withdrawn:", amount)

def check_balance():
    print("Current Balance:", balance)


# Menu
while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == '2':
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == '3':
        check_balance()

    elif choice == '4':
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
