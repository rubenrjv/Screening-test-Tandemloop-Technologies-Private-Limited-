class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Unknown operation"

a_input = float(input("Enter the first number (a): "))
b_input = float(input("Enter the second number (b): "))
operation_input = input("Enter the operation (add, subtract, multiply, divide): ")

calc = Calculator(a_input, b_input, operation_input)

result = calc.calculate()


print("Result:", result)

