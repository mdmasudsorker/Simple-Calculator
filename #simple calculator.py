#simple calculator

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(base, exp):
    return base ** exp

def nth_root(value, n):
    if value < 0 and n % 2 == 0:
        return "Error! Even root of a negative number."
    else:
        return value ** (1 / n)

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Nth Root (y√x)")

    while True:
        choice = input("\nChoose an operation (1-6) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            base = float(input("Enter the base: "))
            exp = float(input("Enter the exponent: "))
            print(f"Result: {base}^{exp} = {power(base, exp)}")

        elif choice == '6':
            value = float(input("Enter the number: "))
            n = int(input("Enter the root (e.g., 2 for square root, 3 for cube root): "))
            print(f"Result: {n}√{value} = {nth_root(value, n)}")

        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
