'''
multiplication table
input:
5
output:
enter a no. :5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50

n = int(input('enter a no. :'))
for i in range(1,11):
    print(f'{n} X {i} = {n*i}')

print amstrong or not

n = int(input("enter a no.:"))
len_ = len(str(n))
am_ = 0
for i in str(n):
    am_ = int(i)**len_ + am_
if am_ == n:
    print(f'{n} is amstrong')
else:
    print(f'{n} not a amstrong')

    
lim = int(input('Enter a no.: '))
n = 0
n1 = 1
print(n,n1,end=' ')
for i in range(1,lim):
    ad = n + n1
    n = n1
    n1 = ad 
    print(ad,end=' ')

Calculater 
input:
5
output:
Enter : 
1.ADD 
2.Sub 
3.Mul 
4.Div 
5.MOd 
6.exit 
2
Enter a No.: 12
Enter a  No.:13
12 - 13 = -1

op = int(input('Enter : \n1.ADD \n2.Sub \n3.Mul \n4.Div \n5.MOd \n6.exit \n'))

if op == 1:
    n = int(input('Enter a No.: '))
    n1 = int(input('Enter a  No.:'))
    print(f'{n} + {n1} = {n+n1}')
elif op == 2:
    n = int(input('Enter a No.: '))
    n1 = int(input('Enter a  No.:'))
    print(f'{n} - {n1} = {n-n1}')
elif op == 3:
    n = int(input('Enter a No.: '))
    n1 = int(input('Enter a  No.:'))
    print(f'{n} X {n1} = {n*n1}')
elif op == 4:
    n = int(input('Enter a No.: '))
    n1 = int(input('Enter a  No.:'))
    print(f'{n} / {n1} = {n/n1}')
elif op == 5:
    n = int(input('Enter a No.: '))
    n1 = int(input('Enter a  No.:'))
    print(f'{n} % {n1} = {n%n1}')
elif op == 6:
    print('Thank you for Using Calculater')
else:
    print("Invalid input")

    
sbi_san = {'Name':'sandeep',
           'atm_pin':'8520',
           'Balance': 78500
}
transactions = []
rem = 3
while rem > 0:
    pin = input("Enter 4 digit pin: ")
    if len(pin) == 4:
        if pin == sbi_san['atm_pin']:
        
            op = int(input('Enter : \n1.Check Balance \n2.WithDraw \n3.Deposit \n4.Transaction\'s \n5.Pin Change \n6.Exit'))
            if op == 1:
                print('Your current Balance = $',sbi_san['Balance'])
            if op == 2:
                amount = int(input('Enter amount to withdraw'))
                if amount <= sbi_san['Balance'] and amount %100 == 0:
                    sbi_san['Balance'] -= amount
                    transactions.append(f"-Withdraw: {amount}")
                    print('collect u r cash')
                    print("remaining balance : $",sbi_san['Balance'])
                else:
                    if amount <= 0:
                        print('invalide amount!')
                    elif amount > sbi_san['Balance']:
                        print('insufficient funds') 
            elif op ==3 :
                amount = float(input("Enter the amount to deposit: $"))
            
                if amount > 0:
                    sbi_san['Balance'] += amount
                    transactions.append(f"-Deposit: {amount}")
                    print(amount, 'deposited successfully')
                    print("updated balance is : $",sbi_san['Balance'])
                else:
                    print('invalide amount!')
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
                            sbi_san.update({'atm_pin': new_pin})
                            print('Pin changed successfully')
                        else:
                            print('Pin did not match')
                    else:
                        print('Pin should be 4 digit ')
                else:
                    print('Incorrect Current pin')


            elif op == 6:
                print('Thank you for using Atm ')
                break
        else:
            rem -= 1
            if rem > 0:
                print(f'Incorrect pin still {rem} attempts lefts')
            else:
                print('Card block')
    else:
        print('Plz enter only 4 digit pin')

'''
