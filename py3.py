def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def run_calculator():
  
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        
        if operation.lower() == 'quit':
            print("Exiting calculator...")
            break
            
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.\n")
            continue

        try:
            # 3. float(input()) -> read numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # 1 & 4. calling defined functions and getting the returned values
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(f"Result: {result}\n")

        # 2. try/except -> catch ValueError and ZeroDivisionError
        except ValueError:
            print("Error: That wasn't a valid number. Please enter digits only.\n")
        except ZeroDivisionError:
            print("Error: You cannot divide by zero. Please try again.\n")

# Run the program
if __name__ == "__main__":
    run_calculator()