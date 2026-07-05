#class name always write in PascalCase

class Student:
    def user_detail(self):
        print("this is user details.")

    def total_mark(self):
        print("this is the total marks.")

    def __str__(self):
        return self

s1 = Student()
s1.user_detail()
s1.total_mark()

# l1 = [1, 2, 3]
# l1.append(79)
# print(l1)
''''
class AddNumber:
    def sum(self, num1, num2):
        return num1 + num2

ob = AddNumber()
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print(ob.sum(a, b))

'''
# Constructor

class Student:
    def __init__(self):
        print("this is constructor.")

s1 = Student()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"\nAccount created successfully for {self.owner}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"\nAccount Holder : {self.owner}")
        print(f"Current Balance: Rs. {self.balance}")


# Create Account
owner = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(owner, balance)

# Menu
while True:
    print("\n========== Bank Menu ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        case 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        case 3:
            account.show_balance()

        case 4:
            print("Thank you for using our banking system.")
            break

        case _:
            print("Invalid choice! Please select between 1 and 4.")