from calculator import Calculator

def main():
    calc = Calculator()
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(f"Result: {calc.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {calc.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {calc.multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"Result: {calc.divide(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()