sbi_sandy = {
    'Name':'Sandeep',
    'account_no':789456123,
    'atm_pin': '8520',
    'balance':100000,
    'transaction':[]
}

def menu():
    print("---------------------------------\n_______-ATM Similutation-_______\n---------------------------------")
    print('\n1.Check Balance \n2.WithDraw \n3.Deposit \n4.Transaction\'s \n5.Pin Change')
    
def check_balance():
    print('Your current Balance = $',sbi_sandy['balance'])

def withdraw():
    amount = int(input("Enter the amount to withdraw: "))
    if amount > sbi_sandy['balance']:
        print('Insufficient Funds!')
    elif amount == 0:
        print("Invalid amount")
    elif amount % 100 != 0:
        print("Amount should be a multiple of 100.")
    else:
        sbi_sandy['balance'] -= amount
        sbi_sandy['transaction'].append(f"-Withdraw : ${amount}")
        print('Collect cash')
        print(f"You withdraw amount is ${amount} and remaining Balance ${sbi_sandy['balance']}")

def deposit():
    amount = int(input("Enter amount to deposit: $"))
    if amount % 100 != 0:
        print("Amount should be a multiple of 100.")
    elif amount == 0:
        print("Invalid amount")
    else:
        sbi_sandy['balance'] += amount
        sbi_sandy['transaction'].append(f'-Deposit : ${amount}')
        print("Amount Deposit Successfully")
        print(f"Updated Balance : ${sbi_sandy['balance']}")

def transaction():
    if len(sbi_sandy['transaction']) == 0:
        print("No Transaction Found!....")
    else:
        print("\n------ Transaction History ------")
        for t in sbi_sandy['transaction']:
            print(t)

def pinchange():
    old_pin = input("Enter Old ATM PIN :")
    if old_pin in sbi_sandy['atm_pin']:
        new_pin = input("Enter New ATM pin : ")
        conform_pin = input("Enter Conform PIN :")
        if len(new_pin) == 4 and new_pin.isdigit():
            if new_pin == conform_pin:
                sbi_sandy['atm_pin'] = new_pin
                print("Pin Changed Successfully")
            else:
                print('Pin does not match')
        else:
            print('Pin must be only 4 digits')

    else:
        print('Invalid pin')

rem = 3
while rem > 0:
    print("---------------------------------\n_______-ATM Similutation-_______\n---------------------------------")
    pin = input("Enter 4 digit pin: ")
    if len(pin) == 4:
        if pin == sbi_sandy['atm_pin']:
            while True:
                menu()
                choice = int(input("Enter Your Chioce: "))
                if choice == 1:
                    check_balance()
                elif choice == 2:
                    withdraw()
                elif choice == 3:
                    deposit()
                elif choice == 4:
                    transaction()
                elif choice == 5:
                    pinchange()
                else:
                    print("Invalid Choice")
                op1 = int(input("_____-ATM Page-______\n1. Home \n2. Exit \nEnter Choice:"))
                if op1  == 1:
                    continue
                elif op1 == 2:
                    print('Thank you for using Atm ')
                    exit()
                else:
                    print("Returning to Home...")
        else:
            rem -= 1
            if rem > 0:
                print(f'Incorrect pin still {rem} attempts left')
            else:
                print("Card block")
    else:
        print("Enter only 4 digit")



print(menu())