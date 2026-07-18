# """
# Python Day 3 – Programming Questions (Data Types)
# Data Types
# Write a program to store an integer, float, string, list, and Boolean value 
# in different variables and print their data types using type().
# a = 10
# b = 10.5
# c = "Hello"
# d = [1, 2, 3]
# e = True
# print(type(a), type(b), type(c), type(d), type(e)) 
# output: <class 'int'> <class 'float'> <class 'str'> <class 'list'> <class 'bool'>

# Write a program to print the memory address of five different variables using id().
# a = 10
# b = 10.5
# c = "Hello"
# d = [1, 2, 3]
# e = True
# print(id(a), id(b), id(c), id(d), id(e))
# output: 140711123456784 140711123456800 140711123456816 140711123456832 140711123456848

# Write a program to compare the memory addresses of two variables having the same integer value.
# a = 10
# b = 10
# c = 10.5
# print(id(a), id(b), id(c))
# output: 140711123456784 140711123456784 140711123456800

# Strings

# Write a program to input your name and print it.
# name =  input("enter you name: ")
# print(name)
# output: enter you name: vamsi
#         vamsi

# Write a program to print each character of a string using indexing.
# name = "vamsi"
# for i in range(len(name)):
#     print(name[i])
# output: v a m s i

# Write a program to print the first and last characters of a string.
# name = "vamsi"
# print(name[0], name[-1])
# output: v i

# Write a program to print the character at a user-given index.
# name = "vamsi"
# index = int(input("Enter an index: "))
# print(name[index])
# output: Enter an index: 2

# Write a program to find the length of a string.
# name = "vamsi"
# print(len(name))
# output: 5

# replace()
# Write a program to replace "World" with "Python" in the string "Hello World".
# a = "Hello World"
# print(a.replace("World", "Python"))
# output: Hello Python

# Write a program to replace all spaces in a sentence with underscores (_).
# a = "Hello everyone"
# print(a.replace(" ", "_"))
# output: Hello_everyone

# Write a program to replace only the first occurrence of "a" with "@".
# a = "banana"
# print(a.replace('a', '@',1))
# output: b@nana

# join()
# Write a program to insert a space between every character of a string using join().
# a = "hello"
# print(' '.join(a))
# output: h e l l o

# Write a program to join all characters of a string using -.
# a = "hello"
# print('-'.join(a))
# output: h-e-l-l-o

# Write a program to join all characters of a string using *.
# a = "hello"
# print('*'.join(a))
# output: h*e*l*l*o

# split()
# Write a program to split a sentence into words.
# a = "hello everyone"
# print(a.split())
# output: ['hello', 'everyone']

# Write a program to split a date (DD-MM-YYYY) into day, month, and year.
# date = '25-04-2002'
# day, month, year = date.split('-')
# print(day, month, year)
# output: 25 04 2002

# Write a program to convert time from 24-hour format to 12-hour format using split().
# time = input("Enter 24h time ")
# time1 = time.split(':')
# print(f'time : {int(time1[0])-12} : {time1[1]} ')
# output : Enter 24h time 22:25
#         time : 10 : 25 

# index()
# Write a program to find the index of the first occurrence of a character entered by the user.
# name = input("enter character :")
# str = "sandeep"
# print(str.index(name))
# #output : enter character :e
#         #4
# Write a program to find the index of "@" in an email address.
# email = "your_email@email.com"
# print(email.index('@'))
# #output : 10

# count()
# Write a program to count the number of vowels in a string using count().
# name = "sandeep"
# vowels = "aeiouAEIOU"
# count_vowels = sum(1 for ch in name if ch in vowels)
# print(count_vowels)
# # output: 3  

# Write a program to count how many times a specific character appears in a string.
# name = "banana"
# character = "a"
# print(name.count(character))
# # output: 3     

# Write a program to count the number of spaces in a sentence.
# name = "hello everyone"
# char = " "
# print(name.count(char))
# #output : 1
# Indexing
# Write a program to print every alternate character of a string.
# name = "python"
# print(name[::2])
# # output: pto

# # Write a program to print the first five characters of a string.
# name = "programming"
# print(name[:5])
# # output: progra

# # Write a program to print the last three characters of a string.
# name = "python"
# print(name[-3:])
# # output: hon

# Lists

# Write a program to create a list containing different data types.
# my_list = [10, 3.5, "Hello", True, [1, 2, 3]]
# print(my_list)
# # output: [10, 3.5, 'Hello', True, [1, 2, 3]]

# # Write a program to print the first, middle, and last elements of a list.
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0], numbers[len(numbers)//2], numbers[-1])
# # output: 10 30 50

# # Write a program to access a nested list element.
# nested = [[1, 2, 3], [4, 5, 6]]
# print(nested[1][2])
# # output: 6

# # Write a program to modify the first element of a list.
# colors = ["red", "green", "blue"]
# colors[0] = "yellow"
# print(colors)
# # output: ['yellow', 'green', 'blue']

# # Write a program to replace the last element of a list with a new value.
# fruits = ["apple", "banana", "cherry"]
# fruits[-1] = "orange"
# print(fruits)
# # output: ['apple', 'banana', 'orange']

# append()
# # Write a program to append one element to a list.
# fruits = ["apple", "banana"]
# fruits.append("cherry")
# print(fruits)
# # output: ['apple', 'banana', 'cherry']

# # Write a program to append a string entered by the user to a list.
# items = []
# value = input("Enter a value: ")
# items.append(value)
# print(items)

# # Write a program to append another list as a single element.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.append(list2)
# print(list1)
# # output: [1, 2, 3, [4, 5, 6]]

# # extend()
# # Write a program to extend a list with another list.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums1.extend(nums2)
# print(nums1)
# # output: [1, 2, 3, 4, 5, 6]

# # Write a program to add multiple numbers to a list using extend().
# numbers = [10, 20]
# numbers.extend([30, 40, 50])
# print(numbers)
# # output: [10, 20, 30, 40, 50]

# # Write a program to extend a list using a string and observe the output.
# letters = ["a", "b"]
# letters.extend("cd")
# print(letters)
# # output: ['a', 'b', 'c', 'd']

# # append() vs extend()
# # Write a program demonstrating the difference between append("Python") and extend("Python").
# word_list = ["Java"]
# word_list.append("Python")
# print(word_list)
# word_list = ["Java"]
# word_list.extend("Python")
# print(word_list)

# # Write a program demonstrating the difference between append([6,7,8]) and extend([6,7,8]).
# list_a = [1, 2]
# list_a.append([6, 7, 8])
# print(list_a)
# list_b = [1, 2]
# list_b.extend([6, 7, 8])
# print(list_b)

# # remove()
# # Write a program to remove a given element from a list.
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)
# # output: ['apple', 'cherry']

# # Write a program to remove the first occurrence of a repeated element.
# nums = [1, 2, 2, 3]
# nums.remove(2)
# print(nums)
# # output: [1, 2, 3]

# # Write a program to remove a user-entered value from a list.
# values = [10, 20, 30]
# remove_value = int(input("Enter a value to remove: "))
# values.remove(remove_value)
# print(values)

# # pop()
# # Write a program to remove an element at a given index using pop().
# items = ["a", "b", "c"]
# items.pop(1)
# print(items)
# # output: ['a', 'c']

# # Write a program to remove the last element using pop().
# colors = ["red", "green", "blue"]
# colors.pop()
# print(colors)
# # output: ['red', 'green']

# # Write a program to store the popped value in another variable and print it.
# letters = ["x", "y", "z"]
# popped_value = letters.pop()
# print(popped_value)
# print(letters)
# # output: z
# # output: ['x', 'y']

# Mixed Programs
# Write a program to create a list of five names and replace one name with another.
# Write a program to create a shopping list and add three new items using append() and extend().
# Write a program to remove duplicate values manually using remove().
# Write a program to split a sentence into words and store them in a list.
# Write a program to join the words of a list using -.
# Write a program to print the type and memory address of every element in a list.
# Write a program to replace all occurrences of "Python" with "Java" in a string.
# Write a program to count the occurrences of each vowel (a, e, i, o, u) in a string using count().
# Write a program to create a nested list and access the deepest element.
# Write a program that demonstrates type(), id(), string methods, and list methods in a single program.
# """
