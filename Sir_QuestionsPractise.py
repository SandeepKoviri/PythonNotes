#q1 check wether a number is positive or negative

# n = int(input("Enter a number: "))
# if n > 0 :
#     print(f'{n} is a positive no.')

# else:
#     print(f'{n} is a negtive no.')

#Q2 check wether a string is palindrome or not 
# str = input("Enter a string: ")
# rev = str[::-1]
# if rev == str:
#     print("its a Palindrom ")
# else:
#     print("Its not a Palindrom")

#Q3 print: 0 1 1 2 3 5 8 13
# limit = int(input("Enter a number: "))

# num1 = 0
# num2 = 1
# print(num1,num2,end=" ")
# for i in range(1,limit):
#     ad = num1 +num2
#     num1 = num2
#     num2 = ad
#     print(ad,end=" ")

#Q4 check age and return true if age is less then 55

# age = int(input("Enter your age :"))
# if age >= 18:
#     print(f" {age} is Eligible")
# else:
#     print(f" {age} Not  Eligible")

#Q5 print: if city = vizag then "A"
#          if city = vijaywada then "B"
#           if city = vizag & vijaywada print "C"
#          if city != vizag & vijaywada print "D"
# city = input("Enter a city name").lower()
# if city == "vizag":
#     print("A")
# elif city == "vijaywada":
#     print("B")
# elif city == "vizag" and city == "vijaywada":
#     print("C")
# elif city != "vizag" and city != "vijaywada":
#     print("D")
# else:
#     print("Invalid Input")

#1.cal are of a rectangle by taking length and width


# leng_ = int(input("Enter lenght: "))
# width = int(input("Enter width:"))

# area = leng_ * width
# print("Area =", area)


#anagram

# a = 'listen'
# b= 'silent'

# if sorted(a) == sorted(b):
#     print(f'{a,b} is anagram')
# else:
#     print(f'{a,b} is not anagram')

#duplicate

# a = input()
# result = ''
# for char in a:
#     if char not in result:
#         result += char
# print(result)

#q1
# print(5&3 , 6&9)
# #output:
# # 1 0
 
# #q2
# for i in range(1515):
#     print("Sandeep")

# #q3
# a = float('85.5')
# b= float(123)
# c = int('9')
# print(a,b,c)
# print(type(a),type(b),type(c))



# # #q4
# n = 4
# for i in range(n):
#     for j in range(n-1):
#         print('*',end="")
#     print()

# #q5
# # 21. Prime and Palindrome Check
# # Question: Write a program to input a number, check whether it is prime, check whether it is a palindrome, and report if it is both.

# num = int(input("Enter a number: "))
# s = str(n)
# pal= s == s[::-1]
# count = 0
# for i in range(1,num+1):
#     if num %i==0:
#         count += 1
# prime = count == 2 

# if prime:
#     print(f"{num} is prime.")
# else:
#     print(f"{num} is not prime.")

# if pal:
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{num} is not a palindrome.")

# if prime and pal:
#     print(f"{num} is both prime and palindrome.")
# else:
#     print(f"{num} is not both prime and palindrome.")


#pattern
#q1
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****

# n = 5
# for i in range(n,0,-1):
#     print('*' * i)
# for i in range(2,n+1):
#     print('*' * i)

#q2
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1

# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

#q3
# a
# ab
# abc
# abcd
# abcde
# abcd
# abc
# ab
# a
# ab
# abc
# abcd
# abcde


# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(chr(64+j), end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, i + 1):
#         print(chr(64+j), end="")
#     print()
# for i in range(2, n + 1):
#     for j in range(1, i + 1):
#         print(chr(64+j), end="")
#     print()

# a
# ab
# abc
# abcd
# abcde
# abcd
# abc
# ab
# a
# ab
# abc
# abcd
# abcde
# n = 5
# letters = 'abcde'
# for i in range(1, n + 1):
#     for j in range(i):
#         print(letters[j], end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print(letters[j], end="")
#     print()
# for i in range(2, n + 1):
#     for j in range(i):
#         print(letters[j], end="")
#     print()

# a
# ab
# abc
# abcd
# abcde
# abcd
# abc
# ab
# a
# leters = 'abcde'
# n = len(leters)
# for i in range(1, n + 1):
#     for j in range(i):
#         print(leters[j], end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print(leters[j], end="")
#     print()


# Write a Python program to calculate the area of a rectangle given its length and width.
# a = int(input("Enter a length of rectangle: "))
# b = int(input("Enter a width of rectangle: "))
# area = a * b
# print("area of a rectangle",area)


# Create a program that takes a user's name and age as input and prints a greeting message.
# name = input("Enter name:")
# age = int(input("Enter age: "))
# print(f" Hello {name}, Welcome to the python world")


# Write a program to check if a number is even or odd.
# a = int(input("Enter a number:"))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("odd")


# Given a list of numbers, find the maximum and minimum values.
# a = [1,2,3,4,5]

# min_ = min(a)
# max_ = max(a)
# print(f"Max{max_} , Min{min_}")

# Create a Python function to check if a given string is a palindrome.
# a = input("Enter a string:").lower()
# b = a[::-1]
# if b == a:
#     print("It's a  palindrome ")
# else:
#     print("print("It's not a palindrome ")")

# Calculate the compound interest for a given principal amount, interest rate, and time period.
# p = int(input("Enter principal amount:"))
# i = int(input("enter Rate of Interest:"))
# t= int(input("Enter time period in years"))
# tot = p * i * t
# ci = tot//100
# print("Compond interest is:",ci)

# Write a program that converts a given number of days into years, weeks, and days.
# Get the total number of days from the user
# t_days = int(input("Enter the number of days: "))

# years = t_days // 365
# remaining_days = t_days % 365
# weeks = remaining_days // 7
# days = remaining_days % 7
# print(f"{t_days} are years:{years},weeks:{weeks},days:{days}")


# Given a list of integers, find the sum of all positive numbers.
# a = [10,20,-30,40,50]
# sum = 0
# for i in a:
#     if i > 0:
#         sum += i
# print(sum)

# Create a program that takes a sentence as input and counts the number of words in it.
# a = input("Enter a string:")
# l = len(a)
# print(l)

# Implement a program that swaps the values of two variables.
# a = int(input("enter a number:"))
# b = int(input("Enter a number:"))
# a, b = b, a
# print(a,b)


