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

