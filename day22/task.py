'''
1. Single vs Multiple

Single Inheritance: One parent → one child.

class A:
    def show(self):
        print("Class A")


class B(A):
    pass


obj = B()
obj.show()

Multiple Inheritance: Multiple parents → one child.

class A:
    def show_a(self):
        print("Class A")


class B:
    def show_b(self):
        print("Class B")


class C(A, B):
    pass


obj = C()
obj.show_a()
obj.show_b()
2. Single vs Multilevel

Single: A → B

class A:
    def show(self):
        print("A")


class B(A):
    pass


B().show()

Multilevel: A → B → C

class A:
    def show_a(self):
        print("A")


class B(A):
    def show_b(self):
        print("B")


class C(B):
    pass


obj = C()
obj.show_a()
obj.show_b()
3. Single vs Hierarchical

Single: One parent → one child.

class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    pass


Child().show()

Hierarchical: One parent → multiple children.

class Parent:
    def show(self):
        print("Parent")


class Child1(Parent):
    pass


class Child2(Parent):
    pass


Child1().show()
Child2().show()
4. Multiple vs Multilevel

Multiple: A + B → C

class A:
    def a(self):
        print("A")


class B:
    def b(self):
        print("B")


class C(A, B):
    pass


obj = C()
obj.a()
obj.b()

Multilevel: A → B → C

class A:
    def a(self):
        print("A")


class B(A):
    def b(self):
        print("B")


class C(B):
    pass


obj = C()
obj.a()
obj.b()
5. Multiple vs Hierarchical

Multiple: Multiple parents → one child.

class Father:
    def father(self):
        print("Father")


class Mother:
    def mother(self):
        print("Mother")


class Child(Father, Mother):
    pass


obj = Child()
obj.father()
obj.mother()

Hierarchical: One parent → multiple children.

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


Dog().eat()
Cat().eat()
6. Multilevel vs Hierarchical

Multilevel: A → B → C

class Grandfather:
    def property(self):
        print("Property")


class Father(Grandfather):
    pass


class Son(Father):
    pass


Son().property()

Hierarchical: A → B and A → C

class Parent:
    def property(self):
        print("Property")


class Son(Parent):
    pass


class Daughter(Parent):
    pass


Son().property()
Daughter().property()
'''