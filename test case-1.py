#13. ATM Transaction Sequence Simulation
balance = 1000

while True:
    print("\n1.Deposit  2.Withdraw  3.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Deposit amount: "))
        balance += amount
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        break
