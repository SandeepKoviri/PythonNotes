'''
---------------
-----day17-----
---6/08/26----
asscii_letters --> this string module function that can give upper and lower letters
digits --> string module function that can give numbers (0-9)
punctuation --> this string module function can give us special characters(!@#$&)

import random
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

o/p:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = '@#$*'

all_chars = letters + digits + special_chars

password = ''
for i in range(5):
    password += random.choice(all_chars)

print(password)

#updating time and date in transaction
bank_balance = 7777

from datetime import datetime
import sys
now = datetime.now()

while True:
    print("--------Welcome to SBI ATM----------")
    user_opt = int(input("\n1.withdraw \n2.deposit \n3.check balance \n4.exit"))
    if user_opt == 1:
        withdraw_money = int(input("enter the money"))
        if withdraw_money > bank_balance:
            bank_balance -= withdraw_money
            print(f'remaining money {bank_balance} {now.strftime("%H:%M %Y-%m-%d")}')
        else:
            print('insufficient money')
    elif user_opt == 2:
        deposit_m = int(input("enter the money you want to deposit"))
        bank_balance += deposit_m
        print(f' money added successfully: {bank_balance} {now.strftime("%H:%M %Y-%m-%d")}')
    elif user_opt == 3:
        print(f'avaiable balance : {bank_balance} {now.strftime("%H:%M %Y-%m-%d")}')
    elif user_opt == 4:
        sys.exit()

    else:
        print("incorrect choice")
        print("thank you for visiting the ATM")
        sys.exit()

#game of choice
import random

comp = random.randint(0,10)
print("----------------------------------------------------------")
print("---------------------Gess The Number----------------------")
print("----------------------------------------------------------")
user = int(input("Enter the number(0-10): "))

if comp == user:
    
    print(f"{comp} and {user}\n U won!..........")
else:
    print(f"{comp} and {user}\nU lost \n/'better luck next time.../'")

'''

