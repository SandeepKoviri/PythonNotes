# Python Day 2 – Programming Questions (Tokens)
# Keywords

# Write a program to print all Python keywords.

# import keyword
# print(keyword.kwlist)
#output : ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue

# Write a program to count the total number of Python keywords.

# import keyword
# count = 0
# for i in keyword.kwlist:
#     count += 1
# print("count =",count)
# output:count = 35

# Write a program to check whether a given word is a Python keyword.
# import keyword
# word = input("enter a keyword :")
# if word in keyword.kwlist:
#     print(word,"is a python keyword")
# else:
#     print(word,"is not a python keyword")
# output : enter a keyword :if
#          if is a python keyword

# Write a program to print each Python keyword on a new line.
# import keyword
# for i in keyword.kwlist:
#     print(i)
# output : False
# none
# True

# Write a program to display the first 10 Python keywords.
# import keyword
# list = keyword.kwlist
# for i in range(10):
#     print(list[i])
    
# Identifiers
# Write a program to declare five valid identifiers and print their values.
# name = "Sandeep"
# age = 21
# city = "Hyderabad"
# roll_no = 101
# is_student = True

# print(name)
# print(age)
# print(city)
# print(roll_no)
# print(is_student)

# Write a program using valid variable, function, and class names.
# student_name = "Asha"

# def greet(name):
#     return "Hello, " + name

# class Student:
#     pass

# print(student_name)
# print(greet("Asha"))
# print(Student)

# Write a program to demonstrate valid and invalid identifiers (by commenting the invalid ones).
# name = "Alice"
# age = 20
# city_name = "Delhi"
# roll_no = 101
# is_student = True

# # invalid identifiers
# # 2name = "Bob"
# # class = "Math"
# # my-name = "Asha"
# # total amount = 50

# print(name)
# print(age)
# print(city_name)
# print(roll_no)
# print(is_student)

# Write a program to create variables for name, age, and city using valid identifiers.
# name ="vamsi"
# age = 25
# city = "vizag"
# print("Name:", name, "Age:", age, "City:", city)

# Write a program to print the values of multiple identifiers.
# name = "Vamsi"
# age = 25
# city = "Vizag"

# print("Name:", name)
# print("Age:", age)
# print("City:", city)

# Arithmetic Operators
# # Write a program to perform addition of two numbers.
# a = 10
# b = 5
# c = a + b
# print("Addition:", c)

# # Write a program to perform subtraction of two numbers.
# c = a - b
# print("Subtraction:", c)

# # Write a program to perform multiplication of two numbers.
# c = a * b
# print("Multiplication:", c)

# # Write a program to perform division of two numbers.
# c = a / b
# print("Division:", c)

# # Write a program to find the remainder using %.
# c = a % b
# print("Remainder:", c)

# # Write a program to find the quotient using //.
# c = a // b
# print("Quotient:", c)

# # Write a program to calculate the square of a number using **.
# c = a ** 2
# print("Square:", c)

# # Write a program to calculate the cube of a number.
# c = a ** 3
# print("Cube:", c)

# # Write a program to calculate the area of a rectangle.
# length = 10
# width = 5
# area = length * width
# print("Area of Rectangle:", area)

# # Write a program to calculate the simple interest.
# principal = 1000
# rate = 5
# time = 2
# simple_interest = (principal * rate * time) / 100
# print("Simple Interest:", simple_interest)

# Assignment Operators

# # Write a program demonstrating the use of +=.
# a = 10
# a += 5
# print("After += operation, a =", a)
# # Write a program demonstrating the use of -=.
# a = 10
# a -= 3
# print("After -= operation, a =", a)
# # Write a program demonstrating the use of *=.
# a = 10
# a *= 2
# print("After *= operation, a =", a)
# # Write a program demonstrating the use of /=.
# a = 10
# a /= 2
# print("After /= operation, a =", a)
# # Write a program demonstrating the use of //=.
# a = 10
# a //= 3
# print("After //= operation, a =", a)
# # Write a program demonstrating the use of %=.
# a = 10
# a %= 3
# print("After %= operation, a =", a)
# # Write a program demonstrating the use of **=.
# a = 10
# a **= 2
# print("After **= operation, a =", a)

# Comparison Operators
# # Write a program to compare two numbers using ==.
# a = 10
# b = 20
# print("Are a and b equal?", a == b)
# # Write a program to compare two numbers using !=.
# print("Are a and b not equal?", a != b)
# # Write a program to check if one number is greater than another.
# print("Is a greater than b?", a > b)
# # Write a program to check if one number is less than or equal to another.
# print("Is a less than or equal to b?", a <= b)
# # Write a program to compare the ages of two people.
# age1 = 25
# age2 = 30
# print("Is age1 greater than age2?", age1 > age2)
# # Write a program to check whether two entered strings are equal.
# string1 = "Hello"
# string2 = "World"
# print("Are string1 and string2 equal?", string1 == string2)

# Logical Operators
# Write a program to check if a person is eligible to vote (age ≥ 18 and citizen).
# age = 20
# print(age >= 18 and True)  # Assuming the person is a citizen
# Write a program to check if a student passes based on marks and attendance.
# stu_marks = 75
# attendance = 85
# print( stu_marks >= 35 and attendance >= 70)

# Write a program using the or operator to check if a student is eligible for a scholarship.
# total_marks = 90
# eligible = total_marks >= 85
# print("Is the student eligible for a scholarship?", eligible)

# Write a program demonstrating the not operator.
# a = True
# print(not(a))  # Output: False
# Write a program to check if a number lies between 10 and 100.
# num = 50
# print(num > 10 and num < 100)  # Output: True
# # Bitwise Operators
# # Write a program to perform bitwise AND on two numbers.
# a = 5
# b = 3
# result = a & b
# print("Bitwise AND of", a, "and", b, "is:", result)
# # Write a program to perform bitwise OR on two numbers.
# result = a | b
# print("Bitwise OR of", a, "and", b, "is:", result)

# # Write a program to perform bitwise XOR on two numbers.
# result = a ^ b
# print("Bitwise XOR of", a, "and", b, "is:", result)

# # Write a program to perform bitwise NOT on a number.
# result = ~a
# print("Bitwise NOT of", a, "is:", result)

# # Write a program to perform left shift (<<) on a number.
# result = a << 2
# print("Left shift of", a, "by 2 positions is:", result)
# # Original
# # 00000101
# # Shift left by 2
# # 00010100
# # Write a program to perform right shift (>>) on a number.
# result = a >> 2
# print("Right shift of", a, "by 2 positions is:", result)
# Membership Operators
# Write a program to check whether a number exists in a list.
# num = [1, 2, 3, 4, 5]
# print(3 in num)  # Output: True
# print(6 in num)  # Output: False
# Write a program to check whether a character exists in a string.
# char = "Hello"
# print('e' in char)  # Output: True
# print('a' in char)  # Output: False
# Write a program to check whether a value is not present in a tuple.
# tup = (1, 2, 3, 4, 5)
# print(6 not in tup)  # Output: True
# Write a program to check whether a key exists in a dictionary.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print('b' in my_dict)  # Output: True

# Write a program to create a bytearray object.
# byte_array = bytearray([65, 66, 67, 68])
# print(byte_array)
# print(type(byte_array))

# Identity Operators
# # Write a program to compare two integers using is and ==.
# a = 10
# b = 10
# print(a is b)  # Output: True
# print(a == b)  # Output: True

# # Write a program to compare two lists using is and ==.
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)  # Output: False
# print(a == b)  # Output: True
# # Write a program to compare two strings using is not.
# a = "Hello"
# b = "Hello"
# print(a is not b)  # Output: False
# Write a program demonstrating the difference between is and ==.
# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)   # True, same values
# print(a is b)   # False, different objects in memory

# Literals
# # Write a program using integer, float, string, and Boolean literals.
# a = 10  # Integer literal
# b = 3.14  # Float literal
# c = "Hello, World!"  # String literal
# d = True  # Boolean literal
# print(type(a), type(b), type(c), type(d))

# Write a program using the None literal.
# a = None
# print(type(a))

# Write a program to create and print a list literal.
# a = [1, 2, 3]
# print(a)

# Write a program to create and print a tuple literal.
# a = (1, 2, 3)
# print(a)

# Write a program to create and print a set literal.
# a = {1, 2, 3}
# print(a)

# Write a program to create and print a dictionary literal.
# a = {'a': 1, 'b': 2, 'c': 3}
# print(a)

# Write a program to create a bytes object.
# a = b"Hello, World!"
# print(a)
# print(type(a))

# Write a program to create a bytearray object.
# a = bytearray([65, 66, 67, 68])
# print(a)
# print(type(a))

# Write a program to create a complex number literal.
# a = 3 + 4j
# print(a)
# print(type(a))

# Write a program to print the data type of every literal using `type()``.
# a = 10  # Integer literal
# b = 3.14  # Float literal
# c = "Hello, World!"  # String literal
# d = True  # Boolean literal
# e = None  # None literal
# f = [1, 2, 3]  # List literal
# g = (1, 2, 3)  # Tuple literal
# print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))