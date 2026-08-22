'''
PANDAS
------
--> pandas are python library used to analysis and manupulation on structured data such as table, csv file
--> to use pandas need to import

eg
--
import pandas as pd
data = pd.Series([1,2,3,4,5,6,7])
print(data)

Functions
---------
1.Series
------
--> this function is a one-dimension labeled data structure
--> the right side is the index values which starts from 0
--> and the other side are normal values

eg
--
import pandas as pd
data = pd.Series([1,2,3,4,5,6,7])
print(data)

Accessing by index
------------------
--> by accessing with the index value and will get data of that index

eg
--
print(data[0])

--> we convert normal dictionary into a struture data by pandas

eg
--
import pandas as pd
stu = {'name':'yash',
       'age':21,
       'batch':7}
det = pd.Series(stu)
print(det)

DataFrame
---------
--> a dataframe is know as 2 dimension labeled data structure in pandas and which contains rows and columns
--> to convert a normal data into a structured data, the data should be given in dictionary
--> in the values we pass list of data

eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme'],
    'product' : ['mobile', 'buds', 'tab'],
    'price':[77777,25000,40000]
}
out = pd.DataFrame(details)
print(out)
print(out['price'])
print(out[['brand','price']])

Methods
-------
head()
------
--> it gives first 5 rows
eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch','neck band','speaker'],
    'price':[77777,25000,40000,200,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.head())

tail()
------
--> it gives last 5 rows
eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch','neck band','speaker'],
    'price':[77777,25000,40000,200,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.tail())

shape
-----
--> used find out the number of rows and columns

eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch','neck band','speaker'],
    'price':[77777,25000,40000,200,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.shape)

info
----
--> this method will gives us total information about the data present 

eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch','neck band','speaker'],
    'price':[77777,25000,40000,200,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.info())

data cleaning
-------------
--> data cleaning is the process of finding problem and fixing it to analysis data

1.missing values
2.incorrect data

isnull()
--------
--> this can find any null values present in data, then it return true

eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch',None,'speaker'],
    'price':[77777,25000,40000,None,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.isnull())

sum()
-----
--> method can find number of null values present in the data
syntax --> variable_name.isnull().sum()

eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch',None,'speaker'],
    'price':[77777,25000,40000,None,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.isnull().sum())

dropna()
--------
--> used to remove the null valued rows from the data
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','vivo','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'tab','charger','watch',None,'speaker'],
    'price':[77777,25000,40000,None,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.dropna())

duplicated()
------------
--> if any same data present it will identify and written true

eg
--
import pandas as pd
details = {
    'brand' : ['apple','samsung','realme','apple','titan','noise','jbl'],
    'product' : ['mobile', 'buds', 'mobile','mobile','watch','neck band','speaker'],
    'price':[77777,25000,40000,77777,30000,2000,5000]
}
out = pd.DataFrame(details)
print(out.duplicated())

reading CSV file
----------------
read.csv()
----------
this can read the csv file data
syntax --> pd.read_csv(file_name)

eg
--
import pandas as pd
re = pd.read_csv("students.csv")
print(re)

'''