"""class Employee:
    def show_details(self):
        print("this is parent method")

class Developer(Employee):
    pass

d1 = Developer()
d1.show_details()"""

#method overloading => same method name but different parameter and data type (this is not allowed in python)

#method overriding =>same method name, data type, argument in both parent and child class

"""class Employee:
    def show_details(self):
        print("this is parent method")

class Developer(Employee):
    def show_details(self):
        print("this is child  method")

d1 = Developer()
d1.show_details()"""



"""class Employee:
    def __init__(self):
        self.user = "ramit"
        self.address = "Kathmandu"

class Developer(Employee):
    def __init__(self):
        self.roll_name = 101

d1 = Developer()
print(d1.user) #this show error due to method overriding"""




class parent:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
class child(parent):
    def add_number(self):
        print(f"the sum is {self.num1+self.num2}")

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
c1 = child(n1,n2)
c1.add_number()