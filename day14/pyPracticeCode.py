# List Comprehension (6 Questions)
# 1. Copy a List
# Question: Write a program using list comprehension to create a new list from an existing list.
# Hint: Use [i for i in list_name].
# Input:
# [1, 2, 3, 4, 5]
# Output:
# [1, 2, 3, 4, 5]

# n = [1, 2, 3, 4, 5]
# new_l = [i for i in n ]
# print(new_l)


# 2. Even Numbers
# Question: Write a program using list comprehension to create a list containing only even numbers.
# Hint: Use if i % 2 == 0.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [2, 4, 6]

# n = [1, 2, 3, 4, 5, 6]
# new_l = [i for i in n if i % 2 == 0]
# print(new_l)

# 3. Odd Numbers
# Question: Write a program using list comprehension to create a list containing only odd numbers.
# Hint: Use if i % 2 != 0.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [1, 3, 5]

# n = [1, 2, 3, 4, 5, 6]
# new_l = [i for i in n if i % 2 != 0]
# print(new_l)


# 4. Replace Odd Numbers
# Question: Write a program using list comprehension to replace every odd number with "Odd".
# Hint: Use if...else inside the comprehension.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# ['Odd', 2, 'Odd', 4, 'Odd', 6]

# n = [1, 2, 3, 4, 5, 6]
# new_l = [i if i%2==0 else 'Odd' for i in n]
# print(new_l)

# 5. Squares of Numbers
# Question: Write a program using list comprehension to create a list of squares from 1 to 10.
# Hint: Use i*i.
# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_l = [i**2 for i in n]
# print(new_l)

# 6. Length of Strings
# Question: Write a program using list comprehension to find the length of each word in a list.
# Hint: Use len() inside the comprehension.
# Input:
# ['Python', 'Java', 'C']
# Output:
# [6, 4, 1]

# n = ['Python', 'Java', 'C']
# new_l = [len(i) for i in n]
# print(new_l)

# Nested List Comprehension (3 Questions)
# 7. Flatten a Nested List
# Question: Write a program to convert a nested list into a single list using nested list comprehension.
# Hint: Use two for loops inside the comprehension.
# Input:
# [[1, 2], [3, 4], [5, 6]]
# Output:
# [1, 2, 3, 4, 5, 6]

# n= [[1, 2], [3, 4], [5, 6]]
# new_l = [i for j in n for i in j]
# print(new_l)

# 8. Multiplication Table
# Question: Write a program using nested list comprehension to generate the multiplication table from 1 to 5.
# Hint: Use two range() loops.
# Output:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]

# new = [[i*j for i in range(1, 6)] for j in range(1, 6)]
# print(new)


# 9. 3×3 Matrix
# Question: Write a program using nested list comprehension to create a 3×3 matrix filled with zeros.
# Hint: Use nested range().
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]

# matrix = [[0 for _ in range(3)] for _ in range(3)]
# print(matrix)

# Generators (3 Questions)
# 10. Square Generator
# Question: Write a generator function that yields the squares of numbers from 1 to n.
# Hint: Use yield inside a for loop.
# Input:
# Enter n: 5
# Output:
# 1
# 4
# 9
# 16
# 25

# n = int(input("Enter n: "))
# def square_gen(n):
#     for i in range(1, n + 1):
#         yield i * i 
# b = square_gen(n)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# 11. Even Number Generator
# Question: Write a generator function that yields even numbers from 1 to n.
# Hint: Use yield only when the number is even.
# Input:
# Enter n: 10
# Output:
# 2
# 4
# 6
# 8
# 10

# n = int(input("Enter n: "))
# def even_gen(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             yield i
# b = even_gen(n)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# 12. Fibonacci Generator
# Question: Write a generator function that yields the Fibonacci series up to n terms.
# Hint: Use yield inside a loop.
# Input:
# Enter terms: 6
# Output:
# 0
# 1
# 1
# 2
# 3
# 5

# n = int(input("Enter terms: "))
# def fibonacci_gen(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# b = fibonacci_gen(n)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# next() Keyword (2 Questions)
# 13. next() with Generator
# Question: Write a generator that yields numbers from 1 to 5 and print each value using next().
# Hint: Create a generator object and call next() repeatedly.
# Output:
# 1
# 2
# 3
# 4
# 5
# def num_gen():
#     for i in range(1, 6):
#         yield i
# n = num_gen()   
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

# 14. Character Generator
# Question: Write a generator that yields each character of a string one by one using yield and retrieve them using next().
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

# n = input("Enter a string: ")
# def char_gen(s):
#     for char in s:
#         yield char

# c = char_gen(n)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))