'''
_______________
day12
29/07/26

default arguments
------------------

eg
def any_(age,edu,name):
    print(age)

any_('teja',67,'msc')
output:
teja

def any_(age,edu,name):
    print(age)

any_(name='teja',age=67,edu='msc')
output:
67

variable length positional arguments
------------------------------------
---> we can pass tuple of arguments and stored in a single parameter by
     just adding *before the parameter..
---> we can access the argument using indixing

def all(*num):
    print(num)
all(10,20,30)
def all(*num):
    print(num[1])
all(10,20,30)
def all(*num):
    print(num[1] + num[2])
all(10,20,30)

variable length keyword arguments
---------------------------------
**kargs
------
---> by pass keyword argument in the argument , will get it as dictionary just add ** before the parameter..
---> and can access by using dictionary methods...
def dct(**num):
    for key, val in num.items():
        print(key,':', val)
dct(name = 'sandy', age= 24 )

both:
----
--->*arg will only flowed by **karg but not karg with *arg
def all(*num,**nums):
    print(num)
    print(nums)
all(10,20,23,name='sandy',age=24,edu='msc')
output:
(10, 20, 23)
{'name': 'sandy', 'age': 24, 'edu': 'msc'}

local and globle variable
------------------------
num1 =23
def all(num1):
    num2 = 20
    print(num2)
    print(num1)
all(num1)
print(num1)

fib

num =0
num1 =1
lim = int(input("Enter a number"))

def fib(num,num1,lim):
    print(num,num1,end=" ")
    for i in range(1,lim +2):
        ad = num + num1
        num = num1
        num1 = ad
        print(ad,end=" ")
        

fib(num,num1,lim)

passing by values
----------------
-->passing direct values in the arguments
def all(a,b):
    print(a,b)
all(0,1)



passing by referance:
--------------------
def all(a,b):
    print(a,b)
all(a=int(input("enter a number:")),b=int(input("enter another num:")))

'''
