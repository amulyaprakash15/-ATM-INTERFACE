class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n✅ ₹{amount} deposited successfully.")
        else:
            print("\n❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n❌ Invalid withdrawal amount.")
        elif amount > self.balance:
            print("\n❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"\n✅ ₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"\n💰 Current balance: ₹{self.balance:.2f}")


class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def display_menu(self):
        print("\n========= ATM Menu =========")
        print("1. 💸 Withdraw")
        print("2. 💰 Deposit")
        print("3. 📊 Check Balance")
        print("4. ❌ Exit")

    def run(self):
        print(f"Welcome, {self.bank_account.account_holder}!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                try:
                    amount = float(input("Enter amount to withdraw: ₹"))
                    self.bank_account.withdraw(amount)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == '2':
                try:
                    amount = float(input("Enter amount to deposit: ₹"))
                    self.bank_account.deposit(amount)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == '3':
                self.bank_account.check_balance()
            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select a valid option.")


# Entry point
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    initial_balance = 0.0
    try:
        initial_balance = float(input("Enter initial balance (₹): "))
    except ValueError:
        print("Invalid input. Starting with ₹0.0 balance.")

    account = BankAccount(user_name, initial_balance)
    atm = ATM(account)
    atm.run()
