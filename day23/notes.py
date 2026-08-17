'''
super() methed
---------------
---> this super method is used to get the constructor from the parent and use in the child class
---> and also can get any method of the parent class


class class_:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class student(class_):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

obj = student("sandeep",24,123456,95)
print(obj.name)
print(obj.rollno)
print(obj.age)
print(obj.marks)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class emp(person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary

obj = emp("sandeep",24,10000)
print(obj.name)
print(obj.age)
print(obj.salary)


class all:
    def job(self):
        print("i'm looking for job")

class looking(all):
    def job1(self):
        super().job()
        print("we are looking for canditate")

any = looking()
any.job1()



Polymorphism
------------
--> polymorphism means a same name but different forms

1. method overloading
---------------------
--> this method overloading happens in class a method is created this same name, but the recent method will be activated and the before one will not be considered

class data :
    def add(self, a,b):
        return a+b

    def add(self, a,b,c):
        return a+b+c

    def add(self, a,b,c,d):
        return a+b+c+d
    
obj = data()
print(obj.add(3,2,1,0))


2. method overriding
--------------------
-->this method overriding happens when parent class and child class have same method and the child class takes its own implementation

class pay :
    def payment(self):
        print('payment called')

class UPI(pay):
    def payment(self):
        print('upi payment called')

class paytm(pay):
    def payment(self):
        print('paytm payment called')
        
obj = UPI()
obj.payment()

go = paytm()
go.payment()

3. operator overloading
-----------------------
--> operator overloading which gives the special meaning to the operator when it is called by object

1.__add__
2.__sub__
3.__mul__
4.__truediv__

eg
--
class cal:
    def __init__(self,a):
        self.a = a
    def __add__(self, a,b):
        print(a+b)

how = cal()
how.__add__(7,7)


eg2
---
class cal:
    def __init__(self,any):
        self.any = any
    def __add__(self, do):
        print(self.any + do.any)

how = cal(77)
who = cal(7)
how.__add__(who)

eg3
---
class cal:
    def __init__(self,any):
        self.any = any
    def __add__(self, do):
        print(self.any + do.any)

how = cal(77)
who = cal(7)
print(how + who)

eg4
---
class cal:
    def __init__(self,any):
        self.any = any
    def __sub__(self, do):
        print(self.any - do.any)

how = cal(77)
who = cal(7)
print(how - who)

eg5
---
class cal:
    def __init__(self,any):
        self.any = any
    def __mul__(self, do):
        print(self.any * do.any)

how = cal(77)
who = cal(7)
print(how * who)


'''


