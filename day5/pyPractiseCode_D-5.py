
# Sets
# Write a program to create a set and print it (with duplicate values).
# so = {1,2,2,3,3,4,4,5,5,}
# print(so)
#output:{1, 2, 3, 4, 5}

# Write a program to create an empty set and print its data type.
# so = set()
# print(so)
# print(type(so))
#output: set()
#<class 'set'>

# Write a program to add a single element to a set using add().
# so = {1,2,3,4}
# so.add(5)
# print(so)
#output:{1, 2, 3, 4, 5}

# Write a program to add multiple elements to a set using update().
# so = {1,2,3,4}
# so.update([5,6])
# print(so)
#output:{1, 2, 3, 4, 5, 6}

# Write a program to remove an element using remove().
# so = {1,2,3,4,5}
# so.remove(2)
# print(so)
#output:{1, 3, 4, 5}

# Write a program to remove an element using discard().
# so = {1,2,3,4}
# so.discard(2)
# print(so)
#output:{1, 3, 4}

# Write a program to remove a random element using pop().
# so = {1,2,3,4,5}
# so.pop()
# print(so)
# #output: {2, 3, 4, 5}

# Set Operations
# Write a program to find the union of two sets.
# a = {1,2,3,4}
# b= {2,3,5,6,7}
# print(a | b)
#output: {1, 2, 3, 4, 5, 6, 7}

# Write a program to find the intersection of two sets.
# a = {1,2,3,4}
# b= {2,3,5,6,7}
# print(a & b)
#output: {2, 3}

# Write a program to find the difference between two sets.
# a = {1,2,3,4}
# b= {2,3,5,6,7}
# print(a - b)
# print(b - a)
# #output: {1, 4}
# #       {5, 6, 7}

# Type Conversion
# Write a program to convert an integer into a string and a float.
# a = 1
# print(type(a))
# b = str(a)
# print(type(b))
# c= float(a)
# print(c)
# #output:
# <class 'int'>
# <class 'str'>
# 1.0

# Write a program to convert a float into an integer and a string.
# a = 9.4
# b= int(a)
# c= str(a)
# print(a,b,c)
# print(type(a),type(b),type(c))
# output:
# 9.4 9 9.4
# <class 'float'> <class 'int'> <class 'str'>

# Write a program to convert a numeric string into an integer and a float.
# a = '67'
# b= int(a)
# c=float(a)
# print(a,b,c)
# print(type(a),type(b),type(c))
# # output:
# 67 67 67.0
# <class 'str'> <class 'int'> <class 'float'>

# Write a program to convert a string into a list and a tuple.
# a = '1234'
# b = list(a)
# c = tuple(a)
# print(a,b,c)
# print(type(a),type(b),type(c))
# #output:
# 1234 ['1', '2', '3', '4'] ('1', '2', '3', '4')
# <class 'str'> <class 'list'> <class 'tuple'>

# Write a program to convert a list into a string and a tuple.
# a = [1,2,3,4]
# b = str(a)
# c = tuple(a)
# print(a,b,c)
# print(type(a),type(b),type(c))
# #output:
# [1, 2, 3, 4] [1, 2, 3, 4] (1, 2, 3, 4)
# <class 'list'> <class 'str'> <class 'tuple'>

# Write a program to convert a tuple into a list and a string.
# a = (1,2,3,4,5)
# b = list(a)
# c = str(a)
# print(a,b,c)
# print(type(a),type(b),type(c))
# #output:
# (1, 2, 3, 4, 5) [1, 2, 3, 4, 5] (1, 2, 3, 4, 5)
# <class 'tuple'> <class 'list'> <class 'str'>

# Concatenation
# Write a program to concatenate two strings using +.
# a = 'python '
# b = 'is a high language'
# print(a + b)
# #output: python is a high language

# Write a program to concatenate two lists using +.
# a = [1,2,3,4]
# b = [4,5,6,7]
# print( a + b)
#output:[1, 2, 3, 4, 4, 5, 6, 7]

# Write a program to concatenate two tuples using +.
# a = (1,2,3,4,5)
# b = (9,8,7,6)
# print(a+b)
# #output:(1, 2, 3, 4, 5, 9, 8, 7, 6)

# Write a program to demonstrate the difference between integer addition (+) and string concatenation (+).
# a = 9
# b = 8
# c = ' 9 '
# d = ' 8 '
# print(a+b)
# print(c+d)
# #output:
# 17
#  9  8 