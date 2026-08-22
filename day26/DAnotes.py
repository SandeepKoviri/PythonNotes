'''
Data Analysis
-------------
--> Data Analysis is the process of collecting, cleaning, transforming, organizing, and analyzing data
to convert into useful information and also used for make decisions to get better outcome

library used
------------
Numpy
Pandas
matplotlib
seaborn

Numpy
-----
--> This refers to numerical python
--> it is a python library used for calculation and operations
--> this python library is more faster then the list to perform operations
--> and also supports multi dimensional arrays

functions
---------
ndim
----
--> the functions is used to find out the dimensions of the array

syntax --> array.ndim

eg
--
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)

eg2
---
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.ndim)
arr_3 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr_3.ndim)

shape
-----
--> the function is used to find out number of rows and columns in array

syntax --> arrray.shape

eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7])
print(arr_2.shape)
arr_3 = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr_3.shape)

reshape
-------
--> function is used to convert one dimension to another if the elements are there to convert into the any dimension

syntax --> array.reshape(row,col)

eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.reshape(2,3))
arr_3 = np.array([
    [1,2,3,4,5,6,7,8,9]
])
print(arr_3.reshape(3,3))

size
----
--> size functions is used to find out the number of elements present in the array

syntax --> array.size

eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.size)

arange
------
--> arange is a function used to generate numbers in a sequence upto a limit and it forms 1D array
--> this array can convert into 2D arrays by using reshape

syntax --> np.arange(range)

eg
--
import numpy as np
arr = np.arange(1,7)
print(arr)
print(arr.reshape(2,3))

Operations
----------
--> same as list we can also perform some operations on arrays
1.indexing
----------
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2[3])

2.slicing
---------
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr_2[3:7])

3.sum
-----
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr_2.sum())

4.add
-----
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
arr = np.array([11,12,13,14,15,16,17,18,19])
print(arr_2 + arr)
print(arr_2 + 7)


5.sub
-----
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
arr = np.array([11,12,13,14,15,16,17,18,19])
print(arr - arr_2)
print(arr_2 - 7)

6.mul
-----
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
arr = np.array([11,12,13,14,15,16,17,18,19])
print(arr_2 * arr)
print(arr_2 * 7)

7.powers
--------
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr_2 ** 7)

8.division
----------
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
arr = np.array([11,12,13,14,15,16,17,18,19])
print(arr_2 / 7)
print(arr / 5)

9.max
-----
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,7,8,9])
arr = np.array([11,12,13,14,15,77,16,17,18,19])
print(arr_2.max())
print(arr.max())

'''
import numpy as np
arr = np.arange(1,10)
arr_2 = arr.reshape(3,3)
print(arr_2.ndim)
print(arr)