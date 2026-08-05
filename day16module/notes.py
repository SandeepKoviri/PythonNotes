'''
----------------
math
---
---> math module used to work on mathematicle functionality

floor
-----
it will round-down to the near value
eg:
import math
print(math.floor(3.14))

ceil
---
--> it will round-up to near value
eg:
import math
print(math.ceil(3.14))

gcd
----
--> it will find gcd value
eg:
import math
print(math.gcd(24,32))

lcm:
----
--> it will find the value of lcm
eg:
import math
print(math.lcm(24,32))

sqrt()
-----
--> we will get the sqrt of the value
eg:
import math
print(math.sqrt(25))

factorial()
----------
--> it will give the value of factorial

eg:
import math
print(math.factorial(5))

import math
print(math.log(5,10))
print(math.cos(math.pi/2))
print(math.pi)


random -module
-------------
--> the random module use to get random number
-randint
------
--> it use to generate random number based on the range

import random

print(random.randint(1,9))

-choice()
---------
---> it will pick the random value from the given data
-shuffle()
--------
---> we can shuffel the data

eg:
import random
print(random.randint(1,9))

colour = ['red','yello','blue','green']
print(random.choice(colour))
random.shuffle(colour)
print(colour)

-uniform()
---------
---> it gives decimal values from the range

eg:
import random

print(random.uniform(1,10))



sys - module
-----------
-version
----------
--> the version of the python interperater
-path
-----
--> .py path we will get by this function

eg:
import sys

print(sys.version)
print(sys.path)


-exit()
--------
--> this is used to exit from the program
-platform()
-----------
--->it will give python run platform
eg:
import sys

print(sys.exit())
print(sys.platform())

-argv
-----
---> it will give the current file run path

eg 
import sys
print(sys.argv)
'''