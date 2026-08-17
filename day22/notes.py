'''
------day22-------
-----14/08/26------
--------------------

Inheritance
-----------
--> Inheritance is the process of inherite one class into another class
--> will general inherite from a class is called parent class and using it in another that class is called child class

class parent:
    def __init__ (self):
        data
    def method(self):
class child(parent)

object = child

eg
--
class company:
    def salary(self):
        print('company salary')

class employee(company):
    def mon_sal(self):
        print('employee salary')

per_sal = employee()
per_sal.mon_sal()
per_sal.salary()

Types
-----
1. single inheritance
---------------------
--> if one child class inherit from one parent class this is called single inheritance


          parent
            |
            |
          child
eg
--
class father:
    def land(self):
        print('7 acer land')

class me(father):
    def flat(self):
        print('7 flat')

all = me()
all.flat()
all.land()

2. multiple inheritance
-----------------------
--> if one child inherite from more than one parent class this is called multiple inheritance
             
    father       mother
       \          /
        \        /
        \      /
        child class
eg
--
class father:
    def home(self):
        print('home at village')

class mother:
    def diamond(self):
        print(' 77 rare diamonds')

class son(father, mother):
    def flat(self):
        print('sons flat')

all = son()
all.flat()
all.diamond()
all.home()

3. multi-level inheritance
--------------------------
--> one child class become parent class to the another class  is called multi-level inheritance

class cls-1:           grand
    def grand(self)      |
class cls-2(cls-1):    father
    def father(self)     |
class cls-3(cls-2):    child
    def son(self)

eg
--
class grandfather:
    def land(self):
        print('land in village')

class father(grandfather):
    def home(self):
        print('home in village')

class son(father):
    def flat(self):
        print('flat in city')

all = son()
all.flat()
all.land()
all.home()
    
4. heirarchical inheritance
---------------------------
--> if two child class inherite from one parent class is called as hierarchical inheritance

               father
                 /\
                /  \
               /    \
          child 1  child 2

eg
--
class father:
    def land(self):
        print('land in village')

class son(father):
    def home(self):
        print('home in city')

class son2(father):
    def flat(self):
        print('flat in city')

all = son()
all.land()
all.home()

all1 = son2()
all1.land()
all1.flat()

5. Hybrid inheritance
---------------------
--> inherite from more than two types into one class is called as hybrid inheritance

      single                   multi
      
     parent class        father     mother
          |                 \       /
          |                  \     /
          |                   \   /  
    child class             child class
            |                   |
              \                /
               \              /
               class (child, child)

class person:
    def name(self):
        print('my name is yaswanth')

class trainee(person):
    def study(self):
        print('da trainee')

class da_teacher:
    def teach(self):
        print('da')

class py_teacher:
    def teach1(self):
        print('py')

class learner(py_teacher, da_teacher):
    def learn(self):
        print('learner')

class all_get(trainee, learner):
    def get_it(self):
        print('this person is getting all data')

an = all_get()
an.name()
an.study()
an.teach()
an.teach1()

'''
'''

class car:
    def bmw(self):
        print("bmw")
class car1(car):
    def odi(self):
        print("odi")
cars = car1()
cars.bmw()
cars.odi()

'''
# 2) Multiple Inheritance : Multiple    
class parents:
    def father(self):
        print("Father")
    def mother(self):
        print("Mother")
class Child1(parents):
    def child1(self):
        print("child")
class Child2(Child1):
    def child2(self):
        print("Child2")

c = Child2()
c.father()
c.mother()
c.child1()
c.child2()