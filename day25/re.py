'''
regular expressions(RegEx)
--------------------------
--> this RegEx is used to form a search pattern to find out the string contain sequence char or not
--> to use this RegEx, we need to import re module

functions
---------
findall
-------
-->the searching pattern is found then, it will gives the o/p in the list[]

eg
--
import re
some = "Python is a programming language"
print(re.findall('[a]', some))

search
------
-->this is also used to form a searching pattern but it will give only the first matched object
-->where it will gives with the index position, where the matched object is found by the pattern

eg
--
import re
some = "python is a programming language"
print(re.search('[a]',some))

eg2
---
import re
do = "i have 777 ruppees in my wallet"
print(re.search('e',do))

meta characters
---------------
--> meta characters are the symbols used in the search pattern

1.[]
----
--> this [] symbol is used find a group char that present in the string, where we can also specify the range

synatx --> re.findall('[range]', variable_name)
-->  by using this symbol we can search cap[A-Z], small[a-z] and digit[0,9]

eg
--
import re
some = "we are in the class room 1"
print(re.findall('[aguo]',some))
print(re.findall('[a-z]', some))
print(re.findall('[0-9]', some))
print(re.search('[a-z]',some))

2..
----
--> thi symbol will refer only one means can match only a single char in pattern

synatx --> re.search('C...', variable_name)

eg
--
import re
some = "Hello everyone"
print(re.findall("H..lo",some))
print(re.search("H..",some))

3.+
---
-->the symbol can find max number of sequence from the string from atleast one character

syntax -->re.findall(".+",variable_name)

eg
--
import re
some = "hello! hello bachooo, aaj hamara topic RegEx"
print(re.findall('h.+a',some))

4.^
---
--> this symbol is used to find the pattern where string starting match or not

syntax --> re.findall("^sequence",variable_name)
eg
--
import re
some = "Hello everyone"
print(re.findall("^Hello",some))
print(re.search("^Hello",some))

5.$
---
-->this symbol will find out if the string is ending with the pattern or not

syntax --> re.findall("sequence$", variable_name)
eg
--
import re
some = "i am planning for a trip"
print(re.findall("trip$",some))
print(re.search("trip$",some))

6.?
---
-->this symbol will find max upto 1 match in the string

syntax --> re.findall('.?',variable_name)

eg
--
import re
some = "hello! hello everyone"
print(re.findall('hel.?o',some))

7.*
---
-->this symbol will find out max number of sequence from the string

syntax --> re.findall('.*',variable_name)

import re
some = "hello! hello bachooo, aaj hamara topic RegEx"
print(re.findall('h.*c',some))

8.{}
----
--> the symbol is used to find a group char that present in string

syntax --> re.finall("E.{size}",variable_name)

eg
--
import re
some = "i am planning for atrip"
print(re.findall("i.{12}",some))

validation for name
-------------------
import re
user_name = input("enter your name:")
pattern = re.findall('^[a-zA-Z]{2,}$',user_name)
if pattern:
    print("correct name")
else:
    print("incorrect name")

validation for indian phone number
----------------------------------
import re
num = input("enter a number:")
pn = re.findall('^[6-9][0-9]{9}$', num)
if pn:
    print("indian number")
else:
    print("not indian")
'''




