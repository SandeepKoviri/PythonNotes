'''
-------day14------
------3/8/26--------
list comprehension, nested comprehension, generator, yield, next     
------------------
list comprehension
------------------
--->list comprehension is the short form of syntax used to generate a new list from the old existing list
syntax: [expression for item in iterable]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_l = [i for i in n ]
print(new_l)
output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_l = [i for i in n if i%2==0]
print(new_l)
output:[2, 4, 6, 8, 10]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_l = [i if i%2==0 else 'Odd' for i in n]
print(new_l)
output:[Odd, 2, Odd, 4, Odd, 6, Odd, 8, Odd, 10]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nel = [i for i in n if i%2!=0]
print(nel)
output:[1, 3, 5, 7, 9]

nested comprehension
-------------------
--->Nested comprehension means an comprehension inside another comprehension. It is used to create a new list from the existing list of lists.

syntax: [expression loop1 and loop2]

match = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
all_ = [i for i in match]
all = [i for j in match for i in j]
print(all_)
print(all)
#output:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

new = [[i*j for i in range(1, 6)] for j in range(1, 6)]
ne = [i for i in range(1, 6)]
print(ne)
print(new)
#output:[1, 2, 3, 4, 5]
#output:[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

generator 
--------
---> this generator will generate the values one at a time and the pause it on the position when we are 
yield keyword
---> hear we will use the yield keyword to get the value

yield keyword
------------
---> this yield() is used to get the value and will only give one value and pause there it self

next keyword
------------
---> this next() keyword is used to get the next value from the generator

def gen(n):
    for i in range(1, n+1):
        yield i*i

b = gen(5)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

output:
1
4
9
16
25

function and generator
----------------------
function
---------
---> returns
---> the value and will return all the values at once
---> in function we will get all values at once 

generator
---------
--->yields
--->when the yield is executed , it will pause the function and 
    the next yield is called it will resume again from the last yield and will give the next value
---> in generator we will one value at a time ..

def gen(n):
    for i in range(1, n+1):
        yield i*i

b = gen(5)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
'''
