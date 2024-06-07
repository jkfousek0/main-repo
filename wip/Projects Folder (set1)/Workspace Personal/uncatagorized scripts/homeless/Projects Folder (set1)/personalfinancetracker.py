# Step 1: Define functions for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Step 2: Create a function to handle user input
def get_user_input():
    print("\nOperations: + (Add), - (Subtract), * (Multiply), / (Divide)")
    operation = input("Choose an operation or type 'exit' to quit: ").strip()

    if operation == 'exit':
        return 'exit', None, None

    if operation not in ('+', '-', '*', '/'):
        print("Invalid operation. Please try again.")
        return None, None, None

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None, None

    return operation, num1, num2

# Step 3 & 4: Implement the main calculator logic with looping
def main():
    while True:
        operation, num1, num2 = get_user_input()

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if operation is None:
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"The result of {num1} {operation} {num2} is: {result}")

# Ensure the main function runs if the script is executed directly
if __name__ == "__main__":
    main()

