"""
___________________________________
----------------20/07/26------------
DAY 5 stes ,set methods, operations on sets, type convertion, concatenation(+)
-set 
    -it is an unodred collection
    - set do not allow duplicate values inside it 
    -set is mutable..
    - set is represented in {}

#example:
do = {1,2,3,2}
print(do)
#output: {1, 2, 3}

for empty set
so = set()
print(type(so))
#output: <class 'set'>

set methods
-----------
-update 
    ---> use to add new value into set
    ---> syntex : variable_name.update(itterable)
    example:
    do = {1,2,3,2}
    do.update([6,8])
    do.update('python')
    print(do)
    #output: {1, 2, 3, 6, 8}
    #output:{1, 2, 3, 'p', 'n', 6, 8, 'h', 'y', 't', 'o'}
- add 
    --->use to add new value into set
    ---> syntex : variable_name.update(value)
    example:
    do = {1,2,3,2}
    do.add('python')
    print(do)
    #output: {1, 2, 3, 'python'}
- Remove
    --->use to del the value from the set , incase if the value is not present in the set it will get key error
    --->syntex:variable_name.remove(value)
    example:
    do = {1,2,3,2}
    do.remove(2)
    print(do)
    #output: {1, 3}

-discard()
    --->use to remove the value from the set , but never give any error incase value is not present in set
    --->syntex:variable_name.discard(value)
    example:
    do = {1,2,3,2}
    do.discard(2)
    print(do)
    output:{1, 3}

-pop()
    --->use to del the value but this pop() will take 0 arguments inside it
    --->syntex:variable_name.pop()
    example:
    do = {5,6,1,2,3,2}
    do.pop()
    print(do)
    output: {2, 3, 5, 6}

-operations on set
-->union   -gives all sets together but no duplicates
        
    example:
    so = {1,2,3,4}
    do = {2,4,5,6}
    print(do|so)
    print(do.union(so))
output:
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}

-->intersection - common values in both sections /sets

example:
    so = {1,2,3,4}
    do = {2,4,5,6}
    print(do&so)
    print(do.intersection(so))
output:
{2, 4}
{2, 4}

-->difference

example:
    so = {1,2,3,4}
    do = {2,4,5,6}
    print(do - so)
    print(so - do)
    print(do.difference(so))
    print(so.difference(do))

output:
{5, 6}
{1, 3}
{5, 6}
{1, 3}

--------------Type convertion---------
int: str; float
_______________
string - str()
eg
    num = 9
    print(type(num))
    so = str(num)
    print(type(so))
output:
<class 'int'>
<class 'str'>

float - float()
eg:
    num = 9
    print(type(num))
    so = float(num)
    print(so)
    print(type(so))
output:
<class 'int'>
9.0
<class 'float'>

float: int;str
--------------
integer - int()
eg:
    num = 9.8
    print(type(num))
    so = int(num)
    print(so)
    print(type(so))
output:
<class 'float'>
9
<class 'int'>

string -- str()
eg:
    num = 9.8
    print(type(num))
    so = str(num)
    print(so)
    print(type(so))
output:
<class 'float'>
9.8
<class 'str'>

string: int;float;list;tuple
-----------------
integer --int()
eg:
    so = '67'
    print(type(so))
    do = int(so)
    print(do)
    print(type(do))
output:
<class 'str'>
67
<class 'int'>
eg:
so = '67 i python' not be converted atherthen integer value str - int
print(type(so))
do = int(so)
print(do)
print(type(do))

float -- float()
eg :
    so = '67.8'
    print(type(so))
    do = float(so)
    print(do)
    print(type(do))
output:
<class 'str'>
67.8
<class 'float'>


list -- list
eg
    so = '1234'
    print(type(so))
    do = list(so)
    print(do)
    print(type(do))
output:
<class 'str'>
['1', '2', '3', '4']
<class 'list'>

tuple -- tuple
eg:
    so = '1234'
    print(type(so))
    do = tuple(so)
    print(do)
    print(type(do))
output:
<class 'str'>
('1', '2', '3', '4')
<class 'tuple'>

list: str;tuple

string -- str()
eg
    so = [1,2,3,4,]
    print(type(so))
    do = str(so)
    print(do)
    print(type(do))
output:
<class 'list'>
[1, 2, 3, 4]
<class 'str'>
tuple -- tuple
eg:
    so = [1,2,3,4,]
    print(type(so))
    do = tuple(so)
    print(do)
    print(type(do))
output:
<class 'list'>
(1, 2, 3, 4)
<class 'tuple'>

tuple: list;str
-----------------
list -- list
eg
    so = (1,2,3,4)
    print(type(so))
    do = list(so)
    print(do)
    print(type(do))
output:
<class 'tuple'>
[1, 2, 3, 4]
<class 'list'>

string -- str()
eg
    so = (1,2,3,4)
    print(type(so))
    do = str(so)
    print(do)
    print(type(do))
output:
<class 'tuple'>
(1, 2, 3, 4)
<class 'str'>

concatenation(+)
----------------

    n = 9
    m = 8
    print(n + m)# it add for integer
    
    n = 'hello'
    m = ' python'
    print(n + m)# it concadnation
    
    q = [1,2]
    r = [3,4]
    print(q+r)

    q = (1,2)
    r = (3,4)
    print(q+r)
output:
17
hello python
[1, 2, 3, 4]
(1, 2, 3, 4)


"""