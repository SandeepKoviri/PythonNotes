
# # Tuple

# # Write a program to create a tuple with different data types and print its type.
# mixed_tuple = (10, "Hello", 3.14, True)
# print("Mixed tuple:", mixed_tuple)
# print("Type of tuple:", type(mixed_tuple))
# #output: Mixed tuple: (10, 'Hello', 3.14, True)
# #       Type of tuple: <class 'tuple'>

# # Write a program to print the first, last, and middle elements of a tuple using indexing.
# numbers = (10, 20, 30, 40, 50)
# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# print("Middle element:", numbers[len(numbers) // 2])
# #output:First element: 10
# #       Last element: 50
# #       Middle element: 30

# # Write a program to access an element from a nested tuple.
# nested_tuple = (1, (2, 3), (4, 5, 6))
# print("Element from nested tuple:", nested_tuple[1][1])
# #output:Element from nested tuple: 3

# # Write a program to access an element inside a list present in a tuple.
# tuple_with_list = (1, [2, 3, 4], 5)
# print("Element inside list in tuple:", tuple_with_list[1][1])
# #output:Element inside list in tuple: 3

# # Write a program to find the index of a given element using index().
# fruits = ("apple", "banana", "cherry", "apple")
# print("Index of 'banana':", fruits.index("banana"))
# #output:Index of 'banana': 1

# # Write a program to count the occurrence of an element using count().
# print("Count of 'apple':", fruits.count("apple"))
# #output: Count of 'apple': 2

# # Write a program to demonstrate that a tuple is immutable.
# immutable_tuple = (1, 2, 3)
# print("Original tuple:", immutable_tuple)
# print("Tuples cannot be changed once created.")
# #output:Original tuple: (1, 2, 3)
# #Tuples cannot be changed once created.

# # Dictionary
# # Write a program to create a dictionary containing student details (name, age, college, marks).
# student = {
#     "name": "Ravi",
#     "age": 20,
#     "college": "ABC College",
#     "marks": 85
# }
# print("Student details:", student)
# #output:Student details: {'name': 'Ravi', 'age': 20, 'college': 'ABC College', 'marks': 85}


# Write a program to print all the keys, values, and items of a dictionary.
student = {
    "name": "Ravi",
    "age": 20,
    "college": "ABC College",
    "marks": 85
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
#output:Keys: dict_keys(['name', 'age', 'college', 'marks'])
#        Values: dict_values(['Ravi', 20, 'ABC College', 85])
#        Items: dict_items([('name', 'Ravi'), ('age', 20), ('college', 'ABC College'), ('marks', 85)])


# Write a program to access the value of a key entered by the user.
key = input("Enter a key (name, age, college, marks): ")
print("Value:", student.get(key, "Key not found"))
#output:Enter a key (name, age, college, marks)
    #Value: Key not found


# Write a program to update the value of an existing key using update().
student.update({"age": 21})
print("Updated age:", student["age"])
#output:Updated age: 21

# Write a program to add a new key-value pair to a dictionary.
student["grade"] = "A"
print("After adding grade:", student)
#output:After adding grade: {'name': 'Ravi', 'age': 21, 'college': 'ABC College', 'marks': 85, 'grade': 'A'}


# Write a program to change the value of a key using dict[key] = value.
student["marks"] = 90
print("Updated marks:", student["marks"])
#output:Updated marks: 90


# Write a program to remove all elements from a dictionary using clear().
student.clear()
print("After clear():", student)
#output:After clear(): {}

# Write a program that demonstrates keys(), values(), items(), update(), and clear() in a single program.
student = {
    "name": "Ravi",
    "age": 20,
    "college": "ABC College",
    "marks": 85
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
student.update({"marks": 88})
print("After update:", student)
student.clear()
print("After clear in final demo:", student)
#output:Keys: dict_keys(['name', 'age', 'college', 'marks'])
#       Values: dict_values(['Ravi', 20, 'ABC College', 85])
#       Items: dict_items([('name', 'Ravi'), ('age', 20), ('college', 'ABC College'), ('marks', 85)])
#       After update: {'name': 'Ravi', 'age': 20, 'college': 'ABC College', 'marks': 88}
#       After clear in final demo: {}