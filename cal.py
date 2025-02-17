def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Welcome to the Python Calculator!")
print("-" * 30)
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("-" * 30)

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("-" * 30)

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            
            print("-" * 30)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            print("-" * 30)

        next_calculation = input("Would you like to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("\n" + "-" * 30)
    else:
        print("Invalid choice. Please select a valid operation.")
        print("-" * 30)
