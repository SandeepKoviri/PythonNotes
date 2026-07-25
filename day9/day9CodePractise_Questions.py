'''
#write even or not for a range
#input:5
#output:
# Enter the limit: 5
# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
limit = int(input("Enter the limit: "))

for i in range(1,limit+1):
    if i%2 ==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

#prime number or not
#input:
#Enter a number: 4
#output:
#4 not a prime
n = int(input('Enter a number: '))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
        # print(count)
if count == 2:
    print(f'{n} is a prime')
else:
    print(f'{n} not a prime')

    
#generate prime no. till 100
for i in range(2,100):
    count = 0
    for j in range(1,i+1):
        if i % j ==0:
            count += 1
    if count == 2:
        print(f'{i} is prime')


#reverse of a string

rev_ = input("Enter a word")
emp = ''
for i in rev_:
    emp = i +emp

if emp == rev_:
    print(f'{rev_} is a palandrom')
else:
    print(f'{rev_} not a palandrom')

#right angle triangle

a = int(input("Enter a NO.:"))
for i in range(1,a+1):
    print('*' * i)
output:
Enter a NO.:5
*
**
***
****
*****

a = int(input("Enter a NO.:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
output:
Enter a NO.:5
*
**
***
****
*****
a = int(input("Enter a NO.:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
output:
Enter a NO.:5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
a = int(input("Enter a NO.:"))
count = 0
for i in range(1,a+1):
    for j in range(1,i+1):
        count += 1
        print(count,end=' ')
    print()
Enter a NO.:5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

a = int(input("Enter a NO.:"))
for i in range(a, 0, -1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
output:
Enter a NO.:5
* * * * * 
* * * * 
* * * 
* * 
* 

count = 0 
a = int(input("Enter a NO.:"))
for i in range(a, 0, -1):
    for j in range(1,i+1):
        count +=1
        print(count,end=' ')
    print()
output:
Enter a NO.:5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 
Enter a NO.:5
1  2  3  4  5  
6  7  8  9  
10  11  12  
13  14  
15 

#triangle
n = int(input())
for j in range(n):
    print(' '*(n - j -1),end='')
    print('* '*(j+1))
for j in range(n,0,-1):
    print(' '*(n - j ),end='')
    print('* '*j)
output:
5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
for i in range(1,n+1):
    print(' '* (n-i-1),end='')
    for j in range(1,i):
        print('* ',end='')
    print()

#remove duplicate's
n = [1,2,3,3,4,4]
emp = []
for i in n:
    if i not in emp:
        emp.append(i)
print(emp)
output:[1, 2, 3, 4]


#perfect no.
n = int(input('Enter a  no.:'))
per = 0
for i in range(1,n):
    if n % i == 0:
        per += i

if  per == n:
    print(f'{n} is a perfect no.')
else:
    print(f'{n} not a perfect no.')
#output:
Enter a  no.28
28 is a perfect no.
'''