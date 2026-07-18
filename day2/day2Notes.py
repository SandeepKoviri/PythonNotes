'''
#___________________________16/07/26______________________
day2 tokens -keywords, identifiers, operater's and literals
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