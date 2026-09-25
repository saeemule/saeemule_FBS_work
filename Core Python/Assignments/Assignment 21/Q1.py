def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid Operator")

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError as ve:
        if str(ve) == "Invalid Operator":
            print("Error: Invalid operator entered. Please use +, -, *, or /")
        else:
            print("Error: Invalid number entered. Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


# ---- Demo ----
calculator()