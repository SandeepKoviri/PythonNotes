from first_M import *
while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus (%)")
    print("6. Power ")
    print("7. cube")
    print("8. Exit")
    choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))
    if choice == 1:
        a = int(input("Enter the 1st no. :"))
        b = int(input("Enter the 2nd no. :"))
        print(add(a,b))
    elif choice == 2:
        a = int(input("Enter the 1st no. :"))
        b = int(input("Enter the 2nd no. :"))
        print(sub(a,b))
    elif choice == 3:
        a = int(input("Enter the 1st no. :"))
        b = int(input("Enter the 2nd no. :"))
        print(mul(a,b))
    elif choice == 4:
        a = int(input("Enter the 1st no. :"))
        b = int(input("Enter the 2nd no. :"))
        print(div(a,b))
    elif choice == 5:
        a = int(input("Enter the 1st no. :"))
        b = int(input("Enter the 2nd no. :"))
        print(mod(a,b))
    elif choice == 6:
        a = int(input("Enter the 1st no. :"))
        print(pow(a))
    elif choice == 7:
        a = int(input("Enter the 1st no. :"))
        print(cube(a))
    elif choice == 8:
        print("Thank you for using the Calculater")
        exit()
    else:
        print("Invalid Choice")