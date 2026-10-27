class BankAccount:

    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(acc_no, name, acc_type, balance)

account.display()

amount = float(input("\nEnter deposit amount: "))
account.deposit(amount)

amount = float(input("Enter withdrawal amount: "))
account.withdraw(amount)

account.display()