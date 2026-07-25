'''

-------22/07/26------
___-output-formate ,statements, if,if else-__
1. camma sepration (,)
----------------------
eg:
name = input()
print('welcome',name)
output: welcome sandeep

eg:
name = input('name: ')
age = int(input("age: "))
print('welcome',name,'your age :',age)
output: welcome sandeep your age : 24

2. f-string (doc-string)
------------------------
eg:
name = input('name: ')
age = int(input("age: "))
print(f"welcome {name} your age : {age}")
output: welcome sandeep your age : 24
%(modules)
----------

%s -->all
%d -->only digit's
%f -->float
eg :
name = 'sandy'
age = 24
price = 89.275868
print('name %s' % name , 'age %d' %age ,'price %f' %price )
output:name sandy age 24 price 89.275868

(dot) .formate()
----------------

eg:
name = 'sandy'
age = 24
price = 89.275868
print('name : {} \nage : {} \nprice :{} '.format(name,age,price))
output: name : sandy 
age : 24 
price :89.275868

statements 
------------
1.conditional statement
--- if ,if else, elif, nested(if)
2.control statement
--- break(exit the loop),
--- countinu(skip the iteration and countinu reast) ,
--- pass(hold the statement)
3. loop
--- for , while


if condition:
------------
----> the if condition is used to check it is True or False
----> syntex: if(condition):
                    statement
eg:
age = int(input('enter age: 18'))
if age >= 18:
    print(f"u r age is {age} u r eligable")
output:
enter age: 18
 u r age is 18 u r eligable

 if else condition:
 ----> else is a fallback statement , incase if condition is false then this else block will execute
 ---->syntex: if condition :
                    statement
              else:
                    statement

 eg :
 age = int(input('enter age: '))
if age >= 18:
    print(f"u r age is {age} u r eligable")
else:
    print(f'u r age {age} ,\nyou have to wait for {18 - age} more years')
output:
enter age: 15
u r age 15 ,
you have to wait for 3 more years

even and odd
num = int(input("enter no: "))
if num %2 == 0:
    print(f'Number {num} is even')
else:
    print(f"Number {num} is odd ")
output:
enter no: 2
Number 2 is even

vowel or consonent with single char:

vol = input("enter single char: ")
if vol in 'AEIOUaeiou':
    print(f'{vol} is vowel')
else:
    print(f'{vol} is consonent')
output:
enter single char: b
b is consonent

palindrom

so = "madam"
do = so[::-1]
if do in so:
    print(f"{so} is palindrom")
else:
    print(f"{so}  not palindrom")
output:
madam is palindrom

leap year or not

year_ = int(input("Enter a year: "))
if year_ %4 == 0 and year_ %100 != 0 or year_ %400 == 0:
    print(f'{year_} is a leap year')
else:
    print(print(f'{year_} not a leap year'))

output:
Enter a year: 2020
2020 is a leap year

mobile is indian or not

mobile_ = input("enter ur monile no: ")
len_ = len(mobile_)
print(len_)
if len_ == 10:
    print(f'{mobile_} is an indian no.')
else:
    print(f'{mobile_} not an indian no.')
output:
10
1234567890 is an indian no.

'''