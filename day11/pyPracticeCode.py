# Python Practice Questions – Day 11 (Functions)
# Functions (4 Questions)
# 1. Addition Function
# Question: Write a user-defined function to add two numbers and print the result.
# Hint: Create a function with two parameters and call it with two arguments.
# Input:
# Enter first number: 15
# Enter second number: 25
# Output:
# Sum = 40

def add_numbers(a, b):
    sum_result = a + b
    print("Sum =", sum_result)


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
add_numbers(first_number, second_number)


# 2. Arithmetic Operations
# Question: Write three user-defined functions to perform addition, subtraction, and multiplication of two numbers.
# Hint: Create three separate functions and call each one.
# Input:
# Enter first number: 20
# Enter second number: 10
# Output:
# Addition = 30
# Subtraction = 10
# Multiplication = 200

def add_numbers(a, b):
    print("Addition =", a + b)


def subtract_numbers(a, b):
    print("Subtraction =", a - b)


def multiply_numbers(a, b):
    print("Multiplication =", a * b)


first_number = 20
second_number = 10
add_numbers(first_number, second_number)
subtract_numbers(first_number, second_number)
multiply_numbers(first_number, second_number)


# 3. Maximum Number
# Question: Write a function to print the greater of two numbers.
# Hint: Use an if-else statement inside the function.
# Input:
# Enter first number: 35
# Enter second number: 42
# Output:
# 42 is greater.

def greater_number(x, y):
    if x > y:
        print(x, "is greater.")
    else:
        print(y, "is greater.")


greater_number(35, 42)


# 4. Even or Odd
# Question: Write a function to check whether a number is even or odd.
# Hint: Use the % operator inside the function.
# Input:
# Enter a number: 18
# Output:
# 18 is an even number.

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is an even number.")
    else:
        print(number, "is an odd number.")


check_even_odd(18)


# Required Arguments (3 Questions)
# 5. Student Details
# Question: Write a function that accepts three required arguments (name, age, course) and prints them.
# Hint: Pass exactly three arguments while calling the function.
# Input:
# Name: Sandeep
# Age: 24
# Course: MCA
# Output:
# Name: Sandeep
# Age: 24
# Course: MCA

def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_details("Sandeep", 24, "MCA")


# 6. Rectangle Area
# Question: Write a function that accepts two required arguments (length and width) and prints the area of a rectangle.
# Hint: Area = length × width.
# Input:
# Length: 10
# Width: 5
# Output:
# Area = 50

def rectangle_area(length, width):
    area = length * width
    print("Area =", area)


rectangle_area(10, 5)


# 7. Full Name
# Question: Write a function that accepts two required arguments (first_name and last_name) and prints the full name.
# Hint: Concatenate the two strings.
# Input:
# First Name: Sandeep
# Last Name: Koviri
# Output:
# Full Name: Sandeep Koviri

def full_name(first_name, last_name):
    print("Full Name:", first_name + " " + last_name)


full_name("Sandeep", "Koviri")


# Positional / Keyword Arguments (3 Questions)
# 8. Employee Details
# Question: Write a function with four parameters (name, id, department, salary) and call it using keyword arguments.
# Hint: Pass the arguments in a different order.
# Input:
# Name = Ravi
# ID = 101
# Department = Python
# Salary = 35000
# Output:
# Name: Ravi
# ID: 101
# Department: Python
# Salary: 35000

def employee_details(name, id, department, salary):
    print("Name:", name)
    print("ID:", id)
    print("Department:", department)
    print("Salary:", salary)


employee_details(name="Ravi", id=101, department="Python", salary=35000)


# 9. Product Details
# Question: Write a function with three parameters (product, price, quantity) and call it using keyword arguments.
# Hint: Change the order while calling the function.
# Input:
# Product = Pen
# Price = 20
# Quantity = 5
# Output:
# Product: Pen
# Price: 20
# Quantity: 5

def product_details(product, price, quantity):
    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)


product_details(product="Pen", price=20, quantity=5)


# 10. Personal Details
# Question: Write a function with five parameters (name, age, city, college, course) and call it using keyword arguments in a different order.
# Hint: Use parameter names while calling the function.
# Input:
# Name = Sandeep
# Age = 24
# City = Visakhapatnam
# College = GVP
# Course = MCA
# Output:
# Name: Sandeep
# Age: 24
# City: Visakhapatnam
# College: GVP
# Course: MCA

def personal_details(name, age, city, college, course):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("College:", college)
    print("Course:", course)


personal_details(name="Sandeep", age=24, city="Visakhapatnam", college="GVP", course="MCA")