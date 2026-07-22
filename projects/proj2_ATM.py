balance = 10000

while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("enter u r choice(1-4): "))

        if choice == 1:
            print('Your current Balance = $',balance)
        
        elif choice ==2 :
            amount = float(input("Enter the amount to deposit: $"))

            if amount > 0:
                balance += amount
                print(amount, 'deposited successfully')
                print("updated balance is : $",balance)
            else:
                print('invalide amount!')
        elif choice == 3:
            amount = float(input("Enter the amount to Withdraw : $"))

            if amount <= 0:
                print('invalide amount!')
            elif amount > balance:
                print('insufficient funds') 
            else:
                balance -= amount
                print('collect u r cash')
                print("remaining balance : $", balance)
        elif choice == 4:
            print('Thank you using')
            break
        else:
            print('Invalide choice! Try again')


