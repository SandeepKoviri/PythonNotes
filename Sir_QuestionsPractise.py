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