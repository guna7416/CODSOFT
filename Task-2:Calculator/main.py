def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values!")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Please choose from +, -, *, /.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")

calculator()
