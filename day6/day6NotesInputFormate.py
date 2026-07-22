'''
__-21/07/26-_____________________________

----------input formate--------

-int - it only take integer to a variable value else throw an error
eg:
n = int(input('Enter a integer :'))
print(n + 9)
print(type(n))
output :
Enter a integer :25
34
<class 'int'>

-string - it will take every thing as an input in '', " " it will show error
----->
eg :
m = input('enter any thing :')
print(m)
print(type(m))
output:
enter any thing :asf46545
asf46545
<class 'str'>

list
-----> 
n = list(map(int,input('enter :').split( )))
print(n)
output:
enter :20 33 35 
[20, 33, 35]

n = input('enter :').split( )
print(n)
output:
enter :apple banana
['apple', 'banana']

n = tuple(map(int,input('enter :').split()))
print(n)
output:
enter :1 2 3 4 5 
(1, 2, 3, 4, 5)

num = eval(input('enter :'))
print(type(num))
output:
enter :8
<class 'int'>

enter :'hekllo'
<class 'str'>

enter :[1,2,3]
<class 'list'>

enter :(1,2,3)
<class 'tuple'>


#string reverse of word 'python'

n = "python"
m = n[::-1]
print(m)
output:
nohtyp
#24h clock into normal

n= tuple(map(int,input("Enter 24h clock").split(':')))
print(n[0] - 12,':',n[1],'PM')
output:
Enter 24h clock24:25
12 : 25 PM

m= input('Enter 24h clock : ')
parts_ = m.split(':')
hour_ = int(m[0] )- 12
print(hour_,' : ',parts_[1],'pm')
output:
Enter 24h clock12:13
0 : 13 PM
s = input()
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] =1
print(freq)
max_freq = max(freq.values())
print(max_freq)
for char in s:
    if freq[char] == max_freq:
        print(char)
        break
#output:
# miiisiiisssion
# i
'''