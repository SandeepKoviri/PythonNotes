# Python Practice Questions – Day 13 (Lambda, map(), filter(), reduce(), return)
# Anonymous (Lambda) Function (3 Questions)
# 1. Add Two Numbers
# Question: Write a lambda function to add two numbers.
# Hint: Use lambda a, b: a + b.
# Input:
# Enter first number: 10
# Enter second number: 20
# Output:
# 30

#code:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# c = lambda a,b :a+b
# print(c(a,b))


# 2. Square of a Number
# Question: Write a lambda function to find the square of a number.
# Hint: Use lambda x: x * x.
# Input:
# Enter a number: 6
# Output:
# 36

#code
# a = int(input("Enter first number: "))
# c = lambda a, :a**2
# print(c(a))

# 3. Largest of Two Numbers
# Question: Write a lambda function to find the greater of two numbers.
# Hint: Use a conditional expression inside the lambda function.
# Input:
# Enter first number: 25
# Enter second number: 18
# Output:
# 25

#code
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# c = lambda a,b : a if a>b else b
# print(c(a,b))

# map() (3 Questions)
# 4. Square of List Elements
# Question: Write a program using map() and lambda to find the square of every element in a list.
# Hint: Apply the lambda function to each list element.
# Input:
# [1, 2, 3, 4, 5]
# Output:
# [1, 4, 9, 16, 25]

#code
# a = [1, 2, 3, 4, 5]
# so = list(map(lambda x: x*x, a))
# print(so)

# 5. Cube of List Elements
# Question: Write a program using map() to find the cube of every element in a list.
# Hint: Use lambda x: x**3.
# Input:
# [1, 2, 3, 4]
# Output:
# [1, 8, 27, 64]

#code
# b = [1, 2, 3, 4]
# so = list(map(lambda x: x**3, b))
# print(so)



# 6. Convert Integers to Strings
# Question: Write a program using map() to convert a list of integers into strings.
# Hint: Use str() inside the lambda function.
# Input:
# [10, 20, 30]
# Output:
# ['10', '20', '30']
# a = [10, 20, 30]
# so = list(map(lambda x: str(x) ,a))
# print(so)


# filter() (3 Questions)
# 7. Even Numbers
# Question: Write a program using filter() to print only the even numbers from a list.
# Hint: Keep numbers where x % 2 == 0.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [2, 4, 6]

#code
# b = [1, 2, 3, 4, 5, 6]
# so = list(filter(lambda x: x%2== 0,b) )
# print(so)

# 8. Odd Numbers
# Question: Write a program using filter() to print only the odd numbers from a list.
# Hint: Keep numbers where x % 2 != 0.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [1, 3, 5]
# b = [1, 2, 3, 4, 5, 6]
# so = list(filter(lambda x: x%2!= 0,b) )
# print(so)

# 9. Numbers Greater Than 50
# Question: Write a program using filter() to print numbers greater than 50.
# Hint: Use the condition x > 50.
# Input:
# [25, 60, 45, 80, 10]
# Output:
# [60, 80]

#code
# a = [25, 60, 45, 80, 10]
# so = list(filter(lambda x: x if x > 50 else 0 ,a))
# print(so)

# reduce() (2 Questions)
# 10. Sum of List Elements
# Question: Write a program using reduce() to find the sum of all elements in a list.
# Hint: Import reduce from functools.
# Input:
# [1, 2, 3, 4, 5]
# Output:
# 15
#code

# from functools import reduce
# a = [1, 2, 3, 4, 5]
# so = reduce(lambda x,y: x+y,a)
# print(so)


# 11. Product of List Elements
# Question: Write a program using reduce() to find the product of all elements in a list.
# Hint: Multiply two elements at a time.
# Input:
# [1, 2, 3, 4]
# Output:
# 24
#code

# a = [1, 2, 3, 4]
# so = reduce(lambda x,y: x*y,a)
# print(so)



# return (2 Questions)
# 12. Addition Using return
# Question: Write a function that returns the sum of two numbers.
# Hint: Use return instead of print().
# Input:
# Enter first number: 12
# Enter second number: 18
# Output:
# 30

#code
# def add(a, b):
#     return a + b
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(add(a, b))


# 13. Largest Number Using return
# Question: Write a function that returns the greater of two numbers.
# Hint: Return the greater value using if-else.
# Input:
# Enter first number: 30
# Enter second number: 25
# Output:
# 30

#code
# def largest(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(largest(a, b))


# Recursion (Factorial) (2 Questions)
# 14. Factorial
# Question: Write a recursive function to find the factorial of a number.
# Hint: Base case: n == 1.
# Input:
# Enter a number: 5
# Output:
# 120

# #code
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# print(factorial(num))


# 15. Fibonacci Using Recursion
# Question: Write a recursive function to print the Fibonacci series up to n terms.
# Hint: Use recursion to calculate each Fibonacci number.
# Input:
# Enter number of terms: 6
# Output:
# 0 1 1 2 3 5

#code
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# terms = int(input("Enter number of terms: "))
# for i in range(terms):
#     print(fibonacci(i), end=' ')

