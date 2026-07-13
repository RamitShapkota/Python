from calcmain import Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

c1 = Calculator(num1, num2)
print("Result:", c1.calculate(operator))