'''
constructer
-----------
--> __init__
--> the constructor is a special method that only run when the object is created
--> mostly we will take data inside this method

eg
--
class cls_data:
    def __init__(self):
        self.name = 'yash'
        self.course = 'python'

cls = cls_data()
print(cls.name)
print(cls.course)

self
----
--> the self keyword refer to current object

eg
--
class stu:
    def __init__(self):
        self.name = 'yash'

    def any(self):
        print(self.name)

s1 = stu()
s1.any()

eg2
---
class stu_data:
    def __init__(self, name, batch, age):
        self.name = name
        self.batch = batch
        self.age = age

    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')

data1 = stu_data('yash', 5, 21)
data1.student()

encapsulation
-------------
--> wrapping data and methods together is called as encapsulation and using or controlling the data in methods

eg
--
class stu_data:
    def __init__(self, name, batch, age):
        self.name = name
        self.batch = batch
        self.age = age

    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')

data1 = stu_data('yash', 5, 21)
data1.student()

access specifiers
-----------------
1. public (name)
----------------
--> this can be access normally and can call it like a normal variable

eg
--
self.name = name
print(self.name)

eg2
---
class stu_data:
    def __init__(self, name, batch, age, fee):
        self.name = name
        self.batch = batch
        self.age = age
        self.fee = fee
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age} and paid {self.fee}')

data1 = stu_data('yash', 5, 21, 45000)
data1.student()

2. protected (_name)
--------------------
--> just adding single(_) before a variable it becomes protected variable

eg
--
self._age = age
print(self._age)

eg2
---
class stu_data:
    def __init__(self, name, batch, age, fee):
        self._name = name
        self._batch = batch
        self._age = age
        self._fee = fee
        
    def only_name(self):
        print(f'{self._name}')

    def only_age(self):
        print(f'{self._age}')

    def only_batch(self):
        print(f'{self._batch}')

    def only_fee(self):
        print(f'{self._fee}')

data1 = stu_data('yash', 5, 21, 45000)
data1.only_name()
data1.only_age()
data1.only_batch()
data1.only_fee()

3. private (__name)
-------------------
--> adding (__) before the variable it becomes private variable

eg
--
self.__balance = balance
print(self.__balance)

eg2
---
class bank:
    def __init__(self):
        self.name = 'yash'
        self.adr = '98765432'
        self.pan = 'fiy34tho3arwhg'
        self.__balance = 34567
        
    def bank_ac(self):
        print(self.name)
        print(self.adr)
        print(self.pan)

    def bank_bal(self):
        print(self.balance)

ac = bank()
ac.bank_ac()

class employee:
    def __init__(self):
        self.name = 'yash'
        self.role = 'da trainee'
        self.__salary = 77777
        self.experience = 7
        self.__emptype = 'part-time'

    def details(self):
        print(self.name)
        print(self.role)

    def income_(self):
        print(self.__salary)

    def type_(self):
        print(self.experience)
        print(self.__emptype)

em = employee()
em.details()
em.income_()
em.type_()
'''

class university:
    def __init__(self):
        self.name = 'yaswanth'
        self.uni = 'woxsen'
        self.batch = 'B.TECH'
        self._specialization = 'CSE'
        self.year = '2022-26'
        self._fees_paid = 23456
        self.__total_fees = 123456

    def details(self):
        print(self.name)
        print(self.uni)
        print(self.batch)

    def fees(self):
        print(self._fees_paid)
        print(self.__total_fees)

    def branch(self):
        print(self.batch)
        print(self._specialization)
        print(self.year)

univ = university()
univ.details()
univ.fees()
univ.branch()