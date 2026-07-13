class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self, operator):
        if operator == "+":
            return self.num1 + self.num2
        
        elif operator == "-":
            return self.num1 - self.num2
        
        elif operator == "*":
            return self.num1 * self.num2
        
        elif operator == "/":
            if self.num2 == 0:
                return "Cannot divide by zero"
            return self.num1 / self.num2
        else:
            return "Invalid operator"