# Function to perform the arithmetic operation
def perform_operation(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '**':
        result = num1 ** num2
    elif operation == '/':
        
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    else:
        return "Error: Invalid operation."

    return f"{num1} {operation} {num2} = {result}"

# Main program
def main():
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Input the operation
    operation = input("Enter the operation (+, -, *, /, **): ")

    # Perform the operation and print the result
    result = perform_operation(num1, num2, operation)
    print(result)

# Run the main program
if __name__ == "__main__":
    main()