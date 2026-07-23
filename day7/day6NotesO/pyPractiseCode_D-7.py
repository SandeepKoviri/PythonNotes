# # Output Formatting (4 Questions)
# # 1. Name and Age (Comma Separation)
# # Question: Write a program to input your name and age and display them using comma (,) separation.
# # Hint: Use input() and print() with commas.
# # Input:
# # Name: Sandeep
# # Age: 24
# # Output:
# # Welcome Sandeep Your age is 24
# #code
# # name = input('enter name: ')
# # age = int(input("enter age: "))
# # print('Welcome ',name,'your age is',age)

# # 2. College Details (f-string)
# # Question: Write a program to input your name, college, and course and display them using an f-string.
# # Hint: Use f"{variable}".
# # Input:
# # Name: Sandeep
# # College: GVP
# # Course: MCA
# # Output:
# # Name: Sandeep
# # College: GVP
# # Course: MCA

# #code:

# # name = input("enter name: ")
# # coll = input('enter college name:')
# # cou = input('course name: ')
# # print(f' Name :{name} \ncollege :{coll} \ncourse :{cou}')

# # 3. Employee Details (% Formatting)
# # Question: Write a program to display employee name, employee ID, and salary using % formatting.
# # Hint: Use %s, %d, and %f.
# # Input:
# # Name: Rahul
# # ID: 101
# # Salary: 35000.50
# # Output:
# # Employee Name: Rahul
# # Employee ID: 101
# # Salary: 35000.500000
# #code:

# # name = input("Name: ")
# # id_ = int(input("Id:"))
# # sal = float(input('Salary :'))
# # print('name: %s'%name,'\nEmployee ID: %d'%id_,'\nSalary: %f'%sal )

# # 4. Product Details (.format())
# # Question: Write a program to input product name, price, and quantity and display them using .format().
# # Hint: Use "{}".format().
# # Input:
# # Product: Pen
# # Price: 15
# # Quantity: 10
# # Output:
# # Product: Pen
# # Price: 15
# # Quantity: 10
# #code:

# # pro = input('prod : ')
# # pri = int(input('price: '))
# # qua = int(input('quantity :'))
# # print('Prodect : {} \nPrice : {} \nQuantiyt :{}'.format(pro,pri,qua))


# # If & If-Else (10 Questions)
# # 5. Voting Eligibility
# # Question: Write a program to check whether a person is eligible to vote.
# # Hint: Age ≥ 18.
# # Input:
# # Age: 20
# # Output:
# # You are eligible to vote.
# # code:
# age = int(input("Enter age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# # 6. Positive or Negative
# # Question: Write a program to check whether a number is positive or negative.
# # Hint: Compare the number with 0.
# # Input:
# # -15
# # Output:
# # -15 is a negative number.
# # code:
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is a positive number.")
# else:
#     print(f"{num} is a negative number.")


# # 7. Even or Odd
# # Question: Write a program to check whether a number is even or odd.
# # Hint: Use % 2.
# # Input:
# # 18
# # Output:
# # 18 is an even number.
# # code:
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")


# # 8. Vowel or Consonant
# # Question: Write a program to check whether a character is a vowel or a consonant.
# # Hint: Check if the character exists in "AEIOUaeiou".
# # Input:
# # e
# # Output:
# # e is a vowel.
# # code:
# ch = input("Enter a character: ")
# if ch in "AEIOUaeiou":
#     print(f"{ch} is a vowel.")
# else:
#     print(f"{ch} is a consonant.")


# # 9. Leap Year
# # Question: Write a program to check whether a given year is a leap year.
# # Hint: Use the leap year condition.
# # Input:
# # 2024
# # Output:
# # 2024 is a leap year.
# # code:
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# # 10. Palindrome
# # Question: Write a program to check whether a given string is a palindrome.
# # Hint: Reverse the string using slicing.
# # Input:
# # madam
# # Output:
# # madam is a palindrome.
# # code:
# text = input("Enter a string: ")
# if text == text[::-1]:
#     print(f"{text} is a palindrome.")
# else:
#     print(f"{text} is not a palindrome.")


# # 11. Mobile Number Validation
# # Question: Write a program to check whether a mobile number is valid (10 digits).
# # Hint: Use len().
# # Input:
# # 9876543210
# # Output:
# # 9876543210 is a valid mobile number.
# # code:
# mobile = input("Enter mobile number: ")
# if len(mobile) == 10 and mobile.isdigit():
#     print(f"{mobile} is a valid mobile number.")
# else:
#     print("Invalid mobile number.")


# # 12. Greater of Two Numbers
# # Question: Write a program to find the greater of two numbers using if-else.
# # Hint: Compare using >.
# # Input:
# # 25
# # 18
# # Output:
# # 25 is greater.
# # code:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(f"{a} is greater.")
# else:
#     print(f"{b} is greater.")


# # 13. Pass or Fail
# # Question: Write a program to check whether a student has passed or failed (pass marks = 35).
# # Hint: Compare marks with 35.
# # Input:
# # 42
# # Output:
# # Student Passed.
# # code:
# marks = int(input("Enter marks: "))
# if marks >= 35:
#     print("Student Passed.")
# else:
#     print("Student Failed.")

# # 14. Uppercase or Lowercase
# # Question: Write a program to check whether a character is uppercase or lowercase.
# # Hint: Compare with 'A'-'Z' or 'a'-'z'.
# # Input:
# # G
# # Output:
# # G is an uppercase letter.
# # code:
# ch = input("Enter a character: ")
# if 'A' <= ch <= 'Z':
#     print(f"{ch} is an uppercase letter.")
# elif 'a' <= ch <= 'z':
#     print(f"{ch} is a lowercase letter.")
# else:
#     print("Invalid character.")


# Mixed Questions (6 Questions)
# 15. Arithmetic Operations
# Question: Write a program to input two numbers and display their sum, difference, product, quotient, floor division, remainder, and power.
# Hint: Use arithmetic operators.
# Input:
# 10
# 5
# Output:
# Sum: 15
# Difference: 5
# Product: 50
# Division: 2.0
# Floor Division: 2
# Remainder: 0
# Power: 100000


# 16. Data Types
# Question: Write a program to create a list, tuple, dictionary, and set, and print the data type of each.
# Hint: Use type().
# Output:
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class 'set'>

# 17. Type Conversion
# Question: Write a program to convert a numeric string into an integer and a float.
# Hint: Use int() and float().
# Input:

# 25

# Output:

# Integer: 25
# Float: 25.0
# 18. Set Operations

# Question: Write a program to create two sets and display their union, intersection, and difference.

# Hint: Use union(), intersection(), and difference().

# Output:

# Union: {1, 2, 3, 4, 5}
# Intersection: {2, 3}
# Difference: {1}
# 19. Dictionary Methods

# Question: Write a program to create a dictionary of student details, update the student's name, and print all keys, values, and items.

# Hint: Use update(), keys(), values(), and items().

# Output:

# Keys: dict_keys(['name', 'age'])
# Values: dict_values(['Sandeep', 24])
# Items: dict_items([('name', 'Sandeep'), ('age', 24)])
# 20. String Methods

# Question: Write a program to input a sentence, split it into words, count the number of spaces, and then join the words using -.

# Hint: Use split(), count(), and join().

# Input:

# I love Python

# Output:

# Words: ['I', 'love', 'Python']
# Spaces: 2
# Joined: I-love-Python