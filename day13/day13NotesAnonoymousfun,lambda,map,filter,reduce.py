'''
--------------
day12
30/07/26
-----------
Anonoymous function
--------------------
---> it is a function that don't have any name
---> this is also called as lambda function
---> lambda function will take n number fo arguments but only one expression

syntex: --> lambda arguments : expression
eg:
so = lambda a: a+10
print(so(5))
output:
15
so = lambda a,b,c: a+b+c
print(so(5,20,30))
output:
55



map()
----> the map function will be applied on the given function 
    of each and every element of an itterable
eg:
num = [1,2,3,4,5]
so = list(map(lambda x : x*x,num))
print(so)
output:
[1, 4, 9, 16, 25]

filter()
--->filter() function will only consider if the condition 
    is true , then it will keep the values
eg:
num = [1,2,3,4,5]
so = list(filter(lambda x : x%2==0,num))
print(so)
output:
[2, 4]

reduce()
---> the reduce function consider all elements and reduce to one single element
---> to use this reduce() u have to import it first from the funtools
eg:
from functools import reduce
num = [1,2,3,4,5]
so = reduce(lambda x,y : x+y,num)
print(so)


print/return
print()
----> it is a inbuild function that is used for diaplay the 
    values stored by variable
return
----> only used inside the functions 
----> when the return is executed then it will exit from the function
    and hold the return value in the calling

factroal
def num(n):
    if n == 1:
        return 1
    return n*num(n-1)
print(num(n=int(input())))

'''


