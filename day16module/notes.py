'''
------day16------
----------------
---5/08/26-----
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


exit
----
--> this function will exit from the program
eg
--
import sys
print(sys.exit())

platform
--------
--> it will give the python run platform

eg
--
import sys
print(sys.platform)

o/p:
win32

argv
----
--> it will give the current file run path

eg
--
import sys
print(sys.argv)

o/p:
['C:\\Users\\rajana yaswanth\\Downloads\\python\\module.py']

datetime
--------
--> used to work with date and time

now
---
--> it will give the today time + date

eg
--
from datetime import datetime, date, time

print(datetime.now())
print(datetime.today())

o/p:
2026-08-05 14:50:39.607454
2026-08-05 14:50:39.655701


from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%m-%d'))
print(now.strftime('%A'))
print(now.strftime('%B'))
print(now.strftime('%H:%M:%S'))

o/p:
2026-08-05
Wednesday
August
14:58:05

%Y --> will get the year
%m --> will get the month
%d --> will get the day
%H --> will get the hour
%M --> will get the minutes
%S --> will get the seconds
%A --> current day
%B --> current month

collections
-----------
-->the collections module will provide container type data which is more powerful than built-in data types (dict, list, tuple)

import collections

data = ['yash', 'raj', 'woxsen', 'uni','yash']
print(collections.Counter(data))

deque
-----
--> used to work with list

eg
--
from collections import deque

how = deque([7,8,9])
how.appendleft(6)
print(how)

o/p:
deque([6, 7, 8, 9])

extend
------

from collections import deque
how = ([1,2,3])
how.extend([4,5,6,7])
print(how)

o/p:
v[1, 2, 3, 4, 5, 6, 7]

pop
---

from collections import deque
how = deque([1,2,3])
how.pop()
print(how)

o/p:
deque([1, 2])

namedtuple
----------

from collections import namedtuple
data = namedtuple("stu",('name','age'))
print(data('yash','21'))

o/p:
stu(name='yash', age='21')

itertools
---------

count
-----

from itertools import count

c = count(76)
for j in range(7):
    print(next(c))

o/p;
76
77
78
79
80
81
82

repeat
------

import itertools
for j in itertools.repeat('yash',7):
    print(j)

o/p:
yash
yash
yash
yash
yash
yash
yash


from itertools import permutations

data = permutations([1,2,3],2)
print(list(data))

o/p:
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import permutations, combinations

data = permutations([1,2,3],2)
print(list(data))

any_ = combinations([1,2,3],2)
print(list(any_))

0/p:
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
[(1, 2), (1, 3), (2, 3)]

import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())

----------
'''
