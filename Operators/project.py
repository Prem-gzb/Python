# Function to show balance

def show_balance(balance):
    print(f"Your current balance is: ${balance}")
    return balance

# Function to make a deposit
def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"${amount} has been deposited.")
        return balance
    else:
        print("Invalid Deposit Amount")
        return 0

# Function to make a withdrawal

def withdrawal(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds!")
    elif amount <= 0:
        print("Invalid Amount")
    else:
        balance -= amount
        print(f"${amount} has been withdrawn.")
    return balance

# Main function that runs the banking operations

def main():
    balance = 0.0  # Starting balance
    while True:
        print("\nBanking System:")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")     

        choice = input("Enter your choice (1/2/3/4): ")
 
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdrawal(balance)
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the main function

if __name__ == "__main__":
    main()