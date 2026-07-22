# Simple Calculator in Python
while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus (%)")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    

    if choice == '6':
        print("Thank you for using the calculator!")
        break
    
    elif choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 + num2)

    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 - num2)

    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 * num2)

    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")

    elif choice == '5':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result =", a % b)
        else:
            print("Error! Modulus by zero is not allowed.")

    else:
        print("Invalid choice! Try again")
    input("\nPress Enter to continue...")