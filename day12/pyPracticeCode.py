'''
Default Arguments (2 Questions)
1. Student Details
Question: Write a function with default values for course and city. 
If the user doesn't pass these values, the default values should be displayed.
Hint: Assign default values in the function definition.
Input:
Name: Sandeep
Age: 24
Output:
Name: Sandeep
Age: 24
Course: MCA
City: Visakhapatnam

def StuDeta(name,age):
    course , City = 'MCA', 'Visakhapatnam'
    print(f'Name = {name} \nAge = {age} \nCourse = {course} \nCity = {City}')
StuDeta(name=input("Name: "),age=int(input("Age :")))

2. Rectangle Area
Question: Write a function to calculate the area of a rectangle where the default width is 5.
Hint: Use a default argument for the width.
Input:
Length: 10
Output:
Area = 50

def area(length):
    width = 5
    area_ = length * width
    print("Area :",area_)
area(length=int(input("Length :")))

Variable Length Positional Arguments (*args) (3 Questions)
3. Sum of Numbers
Question: Write a function that accepts any number of integers using *args and prints their sum.
Hint: *args stores all values as a tuple.
Input:
10 20 30 40
Output:
Sum = 100

def sum_numbers(*args):
    total = 0
    for num in args:
        total += int(num)
    print("Sum =", total)

numbers = input("Input : ").split(',')
sum_numbers(*numbers)

4. Largest Number

Question: Write a function that accepts any number of integers using *args and prints the largest number.
Hint: Use the built-in max() function.
Input:
15 80 25 60
Output:
Largest = 80

def larg(*args):
    n = max(args)
    print(n)
num = input("Enter NUmbers: ").split()
larg(*num)


5. Print Arguments
Question: Write a function that accepts multiple values using *args and prints each value on a separate line.
Hint: Iterate through *args using a loop.
Input:
Python Java C++ Django
Output:
Python
Java
C++
Django

def input_(*args):
    for i in args:
        print(i)
    
values = input("Enter :").split()
input_(*values)

Variable Length Keyword Arguments (**kwargs) (3 Questions)
6. Student Details
Question: Write a function that accepts student details using **kwargs and prints each key and value.
Hint: Use .items().
Input:
name=Sandeep
age=24
course=MCA
Output:
name : Sandeep
age : 24
course : MCA

def all(**kwargs):
    for key, val in kwargs.items():
        print(key ,':', val)
all(Name= input("Name: "),Age = int(input('Age : ')) ,Course=input("Course :"))


7. Employee Details
Question: Write a function using **kwargs to print employee details.
Hint: Loop through the dictionary.
Input:
name=Rahul
salary=35000
department=Python
Output:
name : Rahul
salary : 35000
department : Python

def all(**kwargs):
    for key, val in kwargs.items():
        print(key, ':', val)
all(name='Rahul',salary = 35000, department = 'python')


8. Product Details
Question: Write a function that accepts product details using **kwargs and prints them.
Hint: Access the values using dictionary methods.
Input:
product=Laptop
price=50000
brand=HP
Output:
product : Laptop
price : 50000
brand : HP

def pro_detaile(**kwarg):
    for key, val in kwarg.items():
        print(key, ":", val)
pro_detaile(product = 'Laptop', price = 50000, brand = 'HP')

*args and **kwargs Together (2 Questions)
9. Student Information
Question: Write a function that accepts marks using *args and personal details using **kwargs.
Hint: Print the tuple first and then the dictionary.
Input:
Marks: 85 90 88
Name=Sandeep
Age=24
Output:
Marks: (85, 90, 88)
{'Name': 'Sandeep', 'Age': 24}

def stuInfo(*args, **kwargs):
    print(f'Marks : {args}')
    for key, val in kwargs.items():
        print(key, ":",  val)
stuInfo(80,90,88,Name='Sandeep',Age = 24)

10. Mixed Arguments

Question: Write a function that accepts any number of positional and keyword arguments and prints them.
Hint: Use both *args and **kwargs.
Input:
10 20 30
name=Sandy
city=Vizag
Output:
(10, 20, 30)
{'name': 'Sandy', 'city': 'Vizag'}

def arg(*args, **kwargs):
    print(args)
    print(kwargs)

arg(10,20,30, name='sandy',city= 'vizag')

Local & Global Variables (2 Questions)
11. Local and Global Variable
Question: Write a program to demonstrate the difference between a local variable and a global variable.
Hint: Declare one variable outside the function and another inside it.
Output:
Local Variable: 20
Global Variable: 23

num = 23
def num_(num):
    num1=20
    print('local Variable:',num1)
    print('Globle Variable:',num)
num_(num)

12. Modify Global Variable
Question: Write a program to access a global variable inside a function and print its value.
Hint: Declare the variable outside the function.
Output:
Global Variable = 100

num =100

def a(num):
    print('Global Variable = ',num )
a(num)

Passing Arguments (2 Questions)
13. Passing by Value
Question: Write a function and pass two values directly while calling it.
Hint: Pass numeric values without using variables.
Output:
10 20
def all(a,b):
    print(a,b)
all(10,20)

14. Passing by Reference
Question: Write a function that takes two numbers from the user and prints their sum.
Hint: Pass input() values while calling the function.
Input:
Enter first number: 12
Enter second number: 18
Output:
Sum = 30

def all(a,b):
    print('sum =',a+b)
all(a=int(input("enter a number:")),b=int(input("enter another num:")))

Fibonacci (1 Question)
15. Fibonacci Series
Question: Write a function to print the Fibonacci series up to n terms.
Hint: Initialize the first two numbers as 0 and 1, then generate the remaining terms using a loop.
Input:
Enter number of terms: 7
Output:
0 1 1 2 3 5 8

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
'''