# from test import add_number

# result = add_number(10,20)

# print(f"result is {result}")


def operation(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "%":
        return num1 % num2
    else:
        print("invalid operator")
  