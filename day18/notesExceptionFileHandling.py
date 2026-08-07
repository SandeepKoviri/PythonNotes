'''
Exception Handling
------------------
--> an error can be handled by try and except

1.try:
------
--> we run the code here which may conatin any error
eg
--
try:
    print(n)
except:
    print('some error')

o/p:
some error

2.except:
---------
--> exception can handle any error that come in the try block
eg1
---
try:
    num = 8
    num_2 = 0
    print(num/num_2)
except:
    print('zero division error')\

eg2
---
try:
    num = 0
    num_2 = 6
    print(num_2/num)
except:
    print('will get an error')

num = 8
num_2 = 0
print(num/num_2)

eg3-- if we give string in int type
---
try:
    num = int(input("enter a num:"))
    print(num+9)
except:
    print('will get an error')

eg4-- string and int
---
try:
    print('num'+9)
except:
    print('will get an error')
  
3.else:
-------
-->if no error in the code were raised , then the else block will execute

eg
--
try:
    print(7+7)
except:
    print('error')
else:
    print('no error')

o/p:
14
no error

eg2
---
try:
    print(7+'yash')
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('this will raise zerodivisionerror')
except NameError:
    print('this will raise namerror')
except TypeError:
    print('this will raise typeerror')
else:
    print('no error')

4.finally:
----------
--> the finally block will execute if error present in the try block or not

eg
--
try:
    print(7)
except ZeroDivisionError:
    print('this will raise zerodivisionerror')
except NameError:
    print('this will raise namerror')
except TypeError:
    print('this will raise typeerror')
else:
    print('no error')
finally:
    print('end')

FILE HANDLING
-------------
--> a file handler is an object used to connect with that particular file

1.with(keyword)
---------------
--> by using with keyword no need to close the file, it will close it by itself

syntax
------
with open('file_name'/r'file_path','mode') as name

eg
--
with open(r"C:\Users\koviri\OneDrive\Documents\demo.txt",'r') as file_:
    print(file_.read())

with open('python.txt','r') as file_:
    print(file_.read())

2.open()
--------
--> by using this open() we have to close the file by using close()

eg
--
file = open('python.txt','r')
print(file.read())
file.close()

modes
-----
1.'r'
-----
the 'r' mode is used for functions read(), readline() and readlines()

2.'w'
-----
--> the 'w' mode is used to write() function
3.'a'
-----
--> the 'a' mode is used for write() function and it will add the text at last position

4.'x'

function
--------
1.write()
2.read()
--------
--> the read function will read the file chunk by chunk where we can specify the size
eg
--
with open("py.txt","r") as file:
    print(file.read(20))

3.readline()
------------
--> it will only read one line at a time
eg
--
with open("py.txt","r") as file:
    print(file.readline())

4.readlines()
-------------
--> the readlines() will read whole file and written it in a list, where each line is one index in the list
eg
--
with open("py.txt","r") as file:
    print(file.readlines())



'''
