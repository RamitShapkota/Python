from test1 import operation

# def add_number(a, b):
#     """
#     add tow number   #doc string
#     """
#     return a+b

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter the operator:")


result = operation(num1, num2, op)

print(f"result is {result}")
