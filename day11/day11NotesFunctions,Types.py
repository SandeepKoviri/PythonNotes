'''
__________________
---------day 11---------
-----27/06/26----------


functions:
---------
---> Function is a block that can be executes when we call it.......
---> to avoid the replace lines of code

def function_name(parameters)
    ----
    ----
    ----
function_name(arguments)

types
------
-1. Built In
-----------
--->pre defined by python developers
eg:
print()
max()
len()
min()

-2. User define
--------------
---> user define are the function that are developed by the user
eg:
num = 12
num2 = 23
def add_(num,num2):
    print(num + num2)
def sub (num,num2):
    print(num - num2)
def mul(num , num2):
    print(num * num2)
add_(num, num2)
sub(num, num2)
mul(num, num2)
output:
35
-11
276

Required arguments
--------------------
----> we have to pass same number of arguments that match in the parameters
eg:
num = 12
num2 = 23
def add_(num,num2):
    print(num + num2)
add_(num)
TypeError: add_() missing 1 required positional argument: 'num2'

num = 12
num2 = 23
num3 = 0
def add_(num,num2):
    print(num + num2)
add_(num,num2,num3)

TypeError: add_() takes 2 positional arguments but 3 were given

num = 12
num2 = 23
num3 = 0
def add_(num,num2):
    print(num + num2)
add_(25,26)
add_(num,num2,num3)
output:
51
add_(num,num2,num3)
~~~~^^^^^^^^^^^^^^^
TypeError: add_() takes 2 positional arguments but 3 were given

positonal argument
-----------------
----> it doesn't matter how we are passing the variable , if we assign the value to the variable in the calling....

def name_ (name_,name):
    print(name)
    print(name_)
name_(name= 'sandy', name_ = 'bunny')

output:
sandy
bunny

def pos (e,d,b,c,a):
    print(a,b,c,d,e)
pos(a=5,c=6,d=2,e=2,b=1)
output:
5 1 6 2 2
'''