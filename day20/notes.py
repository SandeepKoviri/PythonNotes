'''
OOPs
----
--> object oriented programming system
--> OOPs is used to maintain the code structure in oject and classes


1. class
--------
--> class is a blueprint or template to an object

syntax
------
class(keyword) Name:
    #attribute
    #methods

eg
--
class person:
    name = 'sandeep'
    age = 21

p1 = person()
print(p1.name)
print(p1.age)
    
2. object
---------
--> object is an instance of the class

syntax
------
class(keyword) Name:
    #attribute
    #methods

any_ = class_name

3. attribute
------------
--> attribute is the data present in the class or pass to the class

eg
--
Take car
--------
color
brand
seat

eg1
---
class sandeep:
    name = 'rajana'
    age = 21
    back_g = 'B.Tech'
ya = sandeep()
print(ya.name)

eg2
---
class car:
    def __init__(self):
        self.color = 'yellow'
        self.seat = 7
        self.brand = 'buggati'

c1 = car()
print(c1.color)
print(c1.brand)

eg3
---
class details:
    def __init__(self):
        self.name = 'yaswanth'
        self.age = 21
        self.back_g = 'B.Tech'
        self.uni = 'woxsen'
        
person_ = details()
print(person_.name)
print(person_.age)
print(person_.back_g)
print(person_.uni)

eg4
---
class bank:
    def __init__(self):
        self.name = 'yaswanth'
        self.age = 21
        self.aadhar = 12345678
        self.pan = 'ehjfv3y89o'
        self.account_number = 2345678
        self.address = 'vizag'
        
person_ = bank()
print(person_.name)
print(person_.age)
print(person_.aadhar)
print(person_.pan)
print(person_.account_number)
print(person_.address)

4. methods
----------
--> method is a function that is created inside the class

syntax
------
class(keyword) name:
    #attributes
    def fun_name(self):
        #code

obj = class_name()
print(obj.fun_name())

eg
--
class student:
    def __init__(self):
        self.name = 'sandeep'
        self.age = 21
        self.course = 'DA'

    def st_name(self):
        print(self.name)
        print(self.age)
        print(self.course)

    def all_data(self):
        print(self.name)
        print(self.age)

stu_ = student()
stu_.st_name()
stu_.all_data()



class car:
    def __init__(self):
        self.color = 'matt black'
        self.seat = 7
        self.brand = 'tata'

    def brake_(self):
        print(f'{self.brand} brake will apply at speed 77km')

    def accelater_(self):
        print(f'{self.brand} will take 2 sec to reach 77 speed')

tata = car()
tata.brake_()
tata.accelater_()

'''
class student:
    def __init__(self, name, age, batch):
            self.name = name
            self.age = age
            self.batch = batch

    def all_(self):
          print(self.name)
          print(self.age)
          print(self.batch)
          
stu1 = student("sandeep",24,"pf5")
stu1.all_()

