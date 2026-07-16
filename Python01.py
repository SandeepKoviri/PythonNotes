''' 
15/04/26

Python was released in the year 1991 by Guido van Russom (version 0.9)

What is Python ?

High-level language 
Object Oriented Programming (OOP's)
Interpreted Language (The code will be executed line by line that's the reason python is called a Interpreted language)
Dynamically Typed Language (No need of mentioning the kind of the datatype pass to the variable)

Why is Python widely used or recommended to be used ?

-Easy to Learn & Understand
-Less Syntax
-Cross Platform 
-Open Source
-Wide range of Libraries

Commenting of the Lines :

Single Line commenting (#) - Used to explain lines in the code
Multiple Line commenting (''' ''' OR """ """) - Used to write the explanation of multiple lines

Variables and Their Rules :

These are used to store the datatypes

Rules : 

It can start with a ( _ , small letters, capital letters, and mixing of the letters, numbers and special characters )
It can't start with a number and special character
The variables can't have whitespaces while being declared but instead we can use a underscore (_) to eliminate those whitespaces


Boolean Type :
These are used to show whether a particular condition is "True" or "False"

Example : 

num , num2 = 9, 89
print(num == num2) # False
print(num != num2) # True

Multiple variables with multiple values ( add , = , )

num , num_2, num_3 = 12, 13, 14
print(num , num_2, num_3)

Multiple variable with single value ( add = = )

num = num_2 = num_3 = 48
print(num , num_2, num_3)

num = 9
num_2 = 90
num , num_2 = num_2 ,num #swaping of two number's without 3rd veriable
print(num)

#16/07/26
            Tokens
            -----
        token's are the smallest individule part or unit of a program which have some meaning in the program.
1. keyword's 35 keywords
-------------
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
   'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
   'return', 'try', 'while', 'with', 'yield']
import keyword
count=0
for i in keyword.kwlist:
    count+=1
print(count)
2. Identifiers
-------------
-variables
- function names
-class names

3. Operators
--------------

1. arthemitic operators
+ , - , * , / , // , % , **
2. assignment operators
= , += , -= , *= , /= , //= , %= , **=
3. comparison operators
== , != , < , > , <= , >=
4. logical operators
and , or , not
num = 8
num_2 = 9
print(num < num_2 and num < num_2)
print(num < num_2 or num > num_2)
print(not(num < num_2 and num < num_2))
print(not(num < num_2 or num > num_2))

5. bitwise operators
& , | , ^ , ~ , << , >>
6. membership operators
in , not in
example :
o = [1,2,3]
print(7 in o)
print(7 not in o)
7. identity operators
is , is not
example :
n = 9
m = 9
o = [1,2,3]
p = [1,2,3]
print(n is m)
print(n == m)
print(o is p)#it checks the memory location of the variable
print(o == p)#this checks the values of the variable

4. Literals
-------------
- String literals
- Numeric literals
- Boolean literals
- Special literals (None)
( int, str, float, complex, bool, bytes, bytearray, list, tuple, set, dict )
'''
print("hello")

print(4 & 5)

