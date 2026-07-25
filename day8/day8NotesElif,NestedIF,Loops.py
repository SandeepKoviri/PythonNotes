'''
_________________________________
------------day 8--------------
--------23/07/2026------------
elif, nested if, loops


elif
----> 
eg:

marks = int(input("Enter marks :"))
if marks >= 35:
    print('pass')
else:
    print('Fail')

if marks >= 90:
    print('A+')
elif marks >=80:
    print('A')
elif marks >=70:
    print('B+')
elif marks >=60:
    print('B')
elif marks >=50:
    print('C+')
elif marks >=40:
    print('C')
elif marks >=35:
    print('D')
else:
    print('Fail')

#greater value of three
#input:
# Enter 1st NO: 25
# Enter 2nd NO: 36
# Enter 3rd NO: 75
#output:
# 75  is grater value

A = int(input("Enter 1st NO: "))
B = int(input("Enter 2nd NO: "))
C = int(input("Enter 3rd NO: "))

if A > B and A > C:
    print(A," is grater value")
elif B > A and B > C :
    print(B," is grater value")
else:
    print(C," is grater value")

Nested if:
---------
detail_ = {'atmpin':'8520'}
atm_ = input("Enter  4 dig atm pin")
if len(atm_) == 4:
    if atm_ == detail_['atmpin']:
        op_ = int(input("Enter \n1.Withdraw \n2.Deposite \n3.Exit"))
        if op_ ==1:
            amount_w = int(input('enter amount for withdraw'))
        elif op_ == 2:
            amount_d = int(input('enter amount for deposit'))
    else:
        print("Incorrect Atm pin entered")

else:
    print("pls enter 4 digit atm pin")
output:
Enter  4 dig atm pin8520
Enter 
1.Withdraw 
2.Deposite 
3.Exit2
enter amount for deposit
_____
control statement:
----------------
break
----> it break the iteration, statement
continue
----> it continues the iteration by skipping paticular iteration if condition is true
num = [10,20,30,40,50]
for i in num:
    if i == 40:
        continue
    print(i) 
else:
    print('end')   
output:
10
20
30
50
end

pass
----> it is used to hold the condition
num = [10,20,30,40,50]
for i in num:
    pass
else:
    print('end') 
_________
loop's
------
-for loop
-while loop

for
--->it used to itereate over sequence such as str, list, tuple
---> else in for loop
            it will execut when the whole iteration is completed
---> incase if condition become true, then else will never execut...

range()
----> this function is used to generate number upto a limit...
--->syntex: range(start,end,step)

for i in range(2,11,2):
    print(i)


eg
num = 'python'
for i in num:
    print(i) 
else:
    print('end')   
output:
p
y
t
h
o
n
end
eg:
num = [10,20,30,40,50]
for i in num:
    print(i) 
    if i == 40:
        break
else:
    print('end')   
output:
10
20
30
40

while
---->
n = 1
while n < 10:
    n += 1
    print(n)

assert keyword
--------------
--> the keyword is used to check the condition
age = 15 next 22
assert age>= 18,'not eligible'
print('eligible')
output:
1.eligible

2.    assert age>= 18,'not eligible'
           ^^^^^^^^
AssertionError: not eligible

n = tuple(map(int,input("Enter 24h time :").split(':')))
if n[0] >= 12 and n[0] <= 24:
    print(f'{n[0] -12}:{n[1]} PM')  
else:
    print(f'{n[0]}:{n[1]} AM')
output:
Enter 24h time :21:36
9:36 PM
Enter 24h time :11:35
11:35 AM
'''