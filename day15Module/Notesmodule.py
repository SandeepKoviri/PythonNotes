'''
--------------
---day 15-----
--08/04/26---
-------------
module
------
--> Module are teh python  code which is saved in (.py) extention
--> which contains functions , variables and classes

type of module
1. Built-in module
---> the built-in module are the module which is already designed with  python when we install python in our system
eg:
math, sys, os, random, datetime, calendar, json, time, statistics

2. user-defined module
---> the user-defined module are the module which is created by the user/ programmer to use in their program
---> syntax: import(keyword) module_name

eg :
fisrt_m.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

next we can use this module in our program by importing it
eg:
import first_M 

print(first_M.add(10,20))
print(first_M.sub(10,20))
print(first_M.mul(10,20))
print(first_M.div(10,20))

-importing with alias name
--------------------------
---> we can import the module with alias name to use in our program
---> after importing the module with alias name ,we have to call the function with alias name in the code
---> syntax: import module_name as alias_name
eg:
import first_M as fm

print(fm.add(10,20))
print(fm.sub(10,20))
print(fm.mul(10,20))
print(fm.div(10,20))

-importing only needed function from module
-----------------------------------
---> we can import only the specific function from the module that we need in our program

from first_M import add,sub,mul,div


print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))

-importing all function from module
-----------------------------------
---> we can import all the function from the module we have to use (* ) in the import statement
--> syntax: from module_name import *
eg:

from first_M import *

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))

-

name = "sandeep"

def get_name():
    print(f"my name is {name}")

we import the module in our program we can use the function get_name() in our program
eg:
from first_M import get_name
get_name()

-random module
-----------------
-->
import random as r

print(r.randint(1000, 9999 ))

-math module
import math as m

print(m.sqrt(25))
sand = {
    'name' : 'sandeep',
    'atm_pin' : '1234'
}
import random
rem = 3
while rem > 0:
    pin = int(input("Enter The pin :"))
    if pin == sand['atm_pin']:
        otp = random.randint(1000,9999) 
        print(otp)
        otp_ = int(input("Enter OTP:"))
        if otp == otp_:
            opt= int(input("Enter choice:"))
        else:
            print("Incorrect Otp:")
            exit()
    else:
        rem -= 1
        if rem > 0:
            print(f'Incorrecty pin {rem} attempts left')
        else:
            print("card block"
'''