''' 
#__________________15/04/26_________________

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

#___________________________16/07/26______________________
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

#__________________17/07/26________________
            data types
            ----------
    to find date type of a variable we can use type() function
    ------>syntex : type( variable_name )
    to find memory location of a variable we can use id() function
    ------>syntex : id( variable_name )

integers - 1, 2, 3, 4, 5# it's not iterable 
floats - 1.0, 2.0, 3.0, 4.0, 5.0
strings
--------
it is a sequence of characters which is enclosed in single quotes(' '), double quotes(" "), triple single quotes(''' ''') or triple double quotes(""" """)
 - "Hello", 'World', '' Python'', """ Programming"""
 it's is immutable--- not modifiable

 it is iterable and indexable

 methods of string
-----------------
replace() - it is used to replace a particular character with another character in a string
    example :               #---------->syntax : variable_name.replace(old_character, new_character, count)#count is optional-- how many times we want to replace the character 
    str = "Hello World"
    print(str.replace("World", "Python"))
    print(str)# immutable 

join() - this method will add the new character after every character of the string
    example :               ---------->syntax : 'new_string'.join(variable_name)
    str = "hello everyone"
    print(' '.join(str))

split() - it is used to split the string into a list of words based on a particular character
    example :               ---------->syntax : variable_name.split(character)
    str = "hello_everyone"
    print(str.split("_"))#output : ['hello', 'everyone']

    time_ = input("Enter the time in 24 hour format : ")
    time =time_.split(":")
    print(f'time: {int(time[0])-12}:{time[1]}:{time[2]} ')

index() - it is used to find the index of a particular character in a string(it tells the first occurence of the character in the string)
    example :               ---------->syntax : variable_name.index(character)
    str = "hello everyone"
    print(str.index("e"))#output : 1
count() - it is used to find the number of occurences of a particular character in a string
    example :               ---------->syntax : variable_name.count(character)
    str = "hello everyone"
    print(str.count("e"))#output : 4
indexing 
    example :               ---------->syntax : variable_name[index]
    str = "hello everyone"
    print(str[0], str[1], str[2])#output : h e l

list - [1, 2, 3, 4, 5]# collection of different data types # it is mutable and iterable 
            representation of list is in square brackets[] and separated by commas ,
    example :               ---------->syntax : variable_name[index]
    list_ = [1, 2, 3, 4, 5, "hello", 3.14, True,[1, 2, [11,"world"],3]]
    print(list_[0], list_[1], list_[5], list_[8], list_[8][2][1][2]) #output : 1 2 hello [1, 2, [11, 'world'], 3] r
    mutable - we can change the values of the list
    example :               ---------->syntax : variable_name[index] = new_value
    list_ = [1, 2, 3, 4, 5]
    list_[0] = 10
    print(list_)#output : [10, 2, 3, 4, 5]
 methods of list
-----------------
append() - it is used to add a new element at the end of the list
    example :               ---------->syntax : variable_name.append(new_element)   
    list_ = [1, 2, 3, 4, 5]
    list_.append(6)
    print(list_)#output : [1, 2, 3, 4, 5, 6]
extend() - it is used to add multiple elements at the end of the list by seprate indexes
    example :               ---------->syntax : variable_name.extend(new_elements)
    list_ = [1, 2, 3, 4, 5]
    list_.extend([6, 7, 8])
    print(list_)#output : [1, 2, 3, 4, 5, 6, 7, 8]

    example :   for difference of append extend
    list_.append("python")
    print(list_)# output : [1, 2, 3, 4, 5, 'python']
    list_.extend("python")
    print(list_)# output : [1, 2, 3, 4, 5, 'python', 'p', 'y', 't', 'h', 'o', 'n']

remove() - it is used to remove a particular element from the list
    example :               ---------->syntax : variable_name.remove(element)
    list_ = [1, 2, 3, 4, 5]
    list_.remove(3)# delete the item based on the value given if not present it will give error
    print(list_)#output : [1, 2, 4, 5]

pop() - it is used to remove a particular element from the list based on the index
    example :               ---------->syntax : variable_name.pop(index)    
    list_ = [1, 2, 3, 4, 5]
    list_.pop(2)# delete the item based on the index position given if not present it will give error(out of range)
    print(list_)#output : [1, 2, 4, 5]
    list_.pop()# delete the last item of the list
    print(list_)#output : [1, 2, 4]

day 4 
------------------18/07/26----------------------
tuple
------
 ----> it a collections of different datatype that are represented in () and seprated by ,
 ----> it's immutable
 methos
 ------
 indexing
 --------   ---->syntex: variable_name[index]
 count
 -----      ---->syntex: variable_name.count(item)
 go = (1,'java', [3,4],("python",78))
 print(type(go))
 print(go.index('java'))
 print(go[2][1])
 print(go.count('python'))#output : 0 because it will not take item inside of inside
 print(go.count(("python",78)))#like this it work
 output:<class 'tuple'>
1
4
0
1

list_ = (1, 2, 3, 4, 5, "hello", 3.14, True,[1, 2, [11,"world"],3])
print(type(list_))
print(list_[0])

dictionary
----------
----> dict is a key:value pair
----> key and values seprated by :
----> dict is represented by {} and pair is seprated by ,
----> only take immuttable values
man = {[1,2]: 5}# error
man = {1:9,
      "name":"sandeep",
      (1,2):5}
print(man)
output:{1: 9, 'name': 'sandeep', (1, 2): 5}

methods
--------
-keys
-----> syntex :dict.keys()
-values
-----> syntex: dict.values()
-items
-----> syntex: dict.items()
-update
----->syntex: dictx.update({key:value})
            details['name'] ='sandeepkoviri'
-clear
------>syntex
example:
details = {
    'name':'sandeep',
    'college':"gvp",
    'pan': 546446,
    'adhr':6876,
    'pin': 1234
}
print(details.keys())
print(details.values())
print(details.items())
details.update({'name':'koviri sandeep'})
details.update({'gender':'male'})
print(details)
details['name'] ='sandeepkoviri'
# details.clear()
print(details)
print(details['name'])#to get
output:
dict_keys(['name', 'college', 'pan', 'adhr', 'pin'])
dict_values(['sandeep', 'gvp', 546446, 6876, 1234])
dict_items([('name', 'sandeep'), ('college', 'gvp'), ('pan', 546446), ('adhr', 6876), ('pin', 1234)])
{'name': 'koviri sandeep', 'college': 'gvp', 'pan': 546446, 'adhr': 6876, 'pin': 1234, 'gender': 'male'}
{'name': 'sandeepkoviri', 'college': 'gvp', 'pan': 546446, 'adhr': 6876, 'pin': 1234, 'gender': 'male'}
sandeepkoviri

'''

details = {
    'name':'sandeep',
    'college':"gvp",
    'pan': 546446,
    'adhr':6876,
    'pin': 1234
}
print(details.keys())
print(details.values())
print(details.items())
details.update({'name':'koviri sandeep'})
details.update({'gender':'male'})
print(details)
details['name'] ='sandeepkoviri'
# details.clear()
print(details)
print(details['name'])#to get