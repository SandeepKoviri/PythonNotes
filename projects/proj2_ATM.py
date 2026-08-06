sbi_san = {'Name':'sandeep',
           'atm_pin':'8520',
           'Balance': 78500
}
import random
from datetime import datetime
now = datetime.now()
transactions = []
rem = 3
while rem > 0:
    pin = input("Enter 4 digit pin: ")
    if len(pin) == 4:
        if pin == sbi_san['atm_pin']:
            otp = random.randint(1000,9999) 
            print(otp)
            otp_ = int(input("Enter OTP:"))
            if otp == otp_:
                print("---------------------------------\n_______-ATM Similutation-_______\n---------------------------------")
                op = int(input('\n1.Check Balance \n2.WithDraw \n3.Deposit \n4.Transaction\'s \n5.Pin Change  \nEnter Your Choice: '))
                if op == 1:
                    print('Your current Balance = $',sbi_san['Balance'])

                elif op == 2:
                    amount = int(input('Enter amount to withdraw : $'))
                    if amount <= sbi_san['Balance'] and amount %100 == 0:
                        sbi_san['Balance'] -= amount
                        transactions.append(f"-Withdraw: {amount},Time:{now.strftime('%t-%m %Y/%m/%d')}")
                        print('collect u r cash')
                        print("remaining balance : $",sbi_san['Balance'])
                    else:
                        if amount <= 0:
                            print('invalide amount!')
                        elif amount > sbi_san['Balance']:
                            print('insufficient funds') 
                elif op ==3 :
                    amount = float(input("Enter the amount to deposit: $"))
            
                    if amount > 0 and amount % 100 == 0:
                        sbi_san['Balance'] += amount
                        transactions.append(f"-Deposit: {amount},Time:{now.strftime('%t-%m %Y/%m/%d')}")
                        print(amount, 'deposited successfully')
                        print("updated balance is : $",sbi_san['Balance'])

                    else:
                        print('invalide amount! or Change can not be deposited')
                elif op == 4:
                    if transactions == 0:
                        print('No transcations Found')
                    else:
                        print('Transaction History')
                        for i in transactions:
                            print(i)


                elif op == 5:
                    old_pin = input('Enter Old pin :')
                    if old_pin in sbi_san['atm_pin']:
                        new_pin = input('Enter New pin to Update: ')
                        conform_pin = input('Conform New Pin :')

                        if len(new_pin) == 4 and new_pin.isdigit():
                            if new_pin == conform_pin:
                                sbi_san['atm_pin'] = new_pin
                                #sbi_san.update({'atm_pin':new_pin})
                                print('Pin changed successfully')
                            else:
                                print('Pin did not match')
                        else:
                            print('Pin should be 4 digit ')
                    else:
                        print('Incorrect Current pin')
                else:
                    print("Invalid Choice")

            else:
                print("Incorrect OTP")
                exit()

            op1 = int(input("_____-ATM Page-______\n1. Home \n2. Exit \nEnter Choice:"))
            if op1  == 1:
                continue
            elif op1 == 2:
                print('Thank you for using Atm ')
                break
            else:
                print("Invalid Choice")

            
        else:
            rem -= 1
            if rem > 0:
                print(f'Incorrect pin still {rem} attempts lefts')
            else:
                print('Card block')
    else:
        print('Plz enter only 4 digit pin')

