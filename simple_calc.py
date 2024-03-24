def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculator():
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}\n")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}\n")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}\n")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"\n{num1} / {num2} = {result}\n")
        elif choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    calculator()
