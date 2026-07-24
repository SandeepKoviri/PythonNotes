# assert keyword
# --------------
# --> the keyword is used to check the condition
# age = 15 next 22
# assert age>= 18,'not eligible'
# print('eligible')
# output:
# 1.eligible

# 2.    assert age>= 18,'not eligible'
#            ^^^^^^^^
# AssertionError: not eligible
#
#24hour clock into 12hours
# n = tuple(map(int,input("Enter 24h time :").split(':')))
# if n[0] >= 12 and n[0] <= 24:
#     print(f'{n[0] -12}:{n[1]} PM')  
# else:
#     print(f'{n[0]}:{n[1]} AM')
# output:
# Enter 24h time :21:36
# 9:36 PM
# Enter 24h time :11:35
# 11:35 AM


# Python Practice Questions – Day 8 (Elif, Nested If, Control Statements, Loops)
# Elif (4 Questions)
# 1. Student Grade
# Question: Write a program to calculate the grade of a student based on marks using if-elif-else.
# Hint: Check marks from highest grade to lowest grade.
# Input:
# Enter marks: 85
# Output:
# Grade: A


# 2. Greatest of Three Numbers
# Question: Write a program to find the greatest of three numbers using if-elif-else.
# Hint: Compare all three numbers.
# Input:
# Enter first number: 25
# Enter second number: 36
# Enter third number: 75
# Output:
# 75 is the greatest number.


# 3. Electricity Bill Category
# Question: Write a program to display the electricity bill category based on units consumed.
# Hint: Use different ranges with elif.
# Input:
# Enter units: 120
# Output:
# Category: Domestic

# units = int(input("Enter units: "))

# if units <= 120:
#     category = "Domestic"
# elif units <= 300:
#     category = "Commercial"
# else:
#     category = "Industrial"

# print(f"Category: {category}")


# 4. Month Name
# Question: Write a program to display the month name based on the month number (1–12).
# Hint: Use if-elif-else.
# Input:
# Enter month number: 8
# Output:
# August
# Nested If (3 Questions)
# a=  int(input("neter a month no: "))
# if a == 1:
#     month = "janvary"
# elif a == 2:
#     month = "february"
# elif a == 3:
#     month = "march"
# elif a == 4:
#     month = "april"
# elif a == 5:
#     month = "may"
# elif a == 6:
#     month = "june"
# elif a == 7:
#     month = "july"
# elif a == 8:
#     month = "august"
# elif a == 9:
#     month = "september"
# elif a == 10:
#     month = "october"
# elif a == 11:
#     month = "november"
# elif a == 12:
#     month = "december"
# else:
#     print("Invalid Input")
# print(f'{a} is {month}')
    

    

# 5. ATM PIN Verification
# Question: Write a program to verify a 4-digit ATM PIN. If the PIN is correct, display a menu (Withdraw, Deposit, Exit).
# Hint: Use an outer if for PIN length and an inner if for PIN verification.
# Input:
# Enter ATM PIN: 8520
# Enter choice: 1
# Output:
# Withdraw Selected
# detail_ = {'atmpin':'8520'}
# atm_ = input("Enter  4 dig atm pin :")
# if len(atm_) == 4:
#     if atm_ == detail_['atmpin']:
#         op_ = int(input("Enter \n1.Withdraw \n2.Deposite \n3.Exit"))
#         if op_ ==1:
#             amount_w = int(input('enter amount for withdraw'))
#         elif op_ == 2:
#             amount_d = int(input('enter amount for deposit'))
#         elif op_ == 3:
#             print("Thank you for using ATM")
            
#     else:
#         print("Incorrect Atm pin entered")

# else:
#     print("pls enter 4 digit atm pin")

# 6. Login Validation
# Question: Write a program to check username and password using nested if.
# Hint: Check username first, then password.
# Input:
# Username: admin
# Password: 1234
# Output:
# Login Successful
# detaile = {'user':'admin',
#            'password':'1234'
#            }
# u = input("Enter User name: ")
# pas_ = input("Enter 4 digit pin :")
# if u in detaile['user'] and pas_ in detaile['password']:
#     print("login Successful")
# else:
#     print("Invalid Cardincial")

# 7. Exam Eligibility
# Question: Write a program to check whether a student is eligible to write an exam based on attendance and fee payment.
# Hint: Use nested if.
# Input:
# Attendance: 80
# Fee Paid: yes
# Output:
# Eligible for Exam


# Control Statements (3 Questions)
# 8. Break

# Question: Write a program to print numbers from 1 to 10 and stop when the number becomes 6.

# Hint: Use break.

# Output:

# 1
# 2
# 3
# 4
# 5
# 6
# 9. Continue

# Question: Write a program to print numbers from 1 to 10, skipping the number 5.

# Hint: Use continue.

# Output:

# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# 10. Pass

# Question: Write a program using pass inside a loop.

# Hint: Use pass as a placeholder.

# Output:

# Loop completed
# For Loop (4 Questions)
# 11. Print Numbers

# Question: Write a program to print numbers from 1 to 10 using a for loop.

# Hint: Use range().

# Output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 12. Even Numbers

# Question: Write a program to print even numbers from 2 to 20.

# Hint: Use range(2, 21, 2).

# Output:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 13. Characters in a String

# Question: Write a program to print each character of a string using a for loop.

# Hint: Iterate through the string.

# Input:

# Python

# Output:

# P
# y
# t
# h
# o
# n
# 14. Sum of First 10 Numbers

# Question: Write a program to find the sum of numbers from 1 to 10 using a for loop.

# Hint: Use an accumulator variable.

# Output:

# Sum = 55
# While Loop (3 Questions)
# 15. Print Numbers

# Question: Write a program to print numbers from 1 to 10 using a while loop.

# Hint: Initialize and increment a variable.

# Output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 16. Multiplication Table

# Question: Write a program to print the multiplication table of a given number using a while loop.

# Hint: Repeat until 10.

# Input:

# Enter number: 5

# Output:

# 5 x 1 = 5
# ...
# 5 x 10 = 50
# 17. Countdown

# Question: Write a program to print a countdown from 10 to 1 using a while loop.

# Hint: Decrement the variable.

# Output:

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Mixed Practice (3 Questions)
# 18. 24-Hour to 12-Hour Time

# Question: Write a program to convert time from 24-hour format to 12-hour format.

# Hint: Use split(), tuple(), and if-else.

# Input:

# Enter time: 18:30

# Output:

# 6:30 PM
# 19. Assert Keyword

# Question: Write a program to check whether a person is eligible to vote using the assert keyword.

# Hint: Use assert age >= 18.

# Input:

# Age: 20

# Output:

# Eligible
# 20. Mixed Program

# Question: Write a program that:

# Takes a list of numbers.
# Prints only even numbers using a for loop.
# Skips one specific number using continue.
# Stops the loop when a given number is found using break.

# Hint: Use if, continue, and break together.

# Sample Input:

# [2, 4, 6, 8, 10, 12]

# Sample Output:

# 2
# 4
# 8