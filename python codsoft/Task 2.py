def calculator():
    print("Simple Calculator \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")

    while True:
        choice = int(input("Enter your choice (1-5): "))

        if choice in range(1, 5):
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            if choice == 1:
                result = number1 + number2
                print("Result:", result)
            elif choice == 2:
                result = number1 - number2
                print("Result:",result)
            elif choice == 3:
                result = number1 * number2
                print("Result:",result)
            elif choice == 4:
                if number2 != 0:
                    result = number1 / number2
                    print("Result:",result)
                else:
                    print("Error! Division by zero is not allowed.")
        elif choice == 5:
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

calculator()
