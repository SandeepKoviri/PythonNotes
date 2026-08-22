'''
matplotlib
----------
--> this is a python library used to create graphs and chats

plot
----
--> the function can create a line graphs with driven data

xlabel
------
--> used to represent the x-axis values

ylabel
------
--> used to represent the y-axis values

title
-----
--> to define the title of the graph

bar graph
---------
import matplotlib.pyplot as plt

views=[1200,2400,200,500]
sport =['cricket','football','badmintion','tennis']
plt.barh(sport, views, color = 'yellow')
plt.xlabel('sports')
plt.ylabel('views in millions')
plt.title('viewrship')
plt.show()

pie chart
---------
import matplotlib.pyplot as plt

views=[1200,2400,200,500]
sport =['cricket','football','badmintion','tennis']
plt.pie(views, labels=sport)
plt.title('viewrship')
plt.legend(sport)
plt.show()

scatter graph
-------------
import matplotlib.pyplot as plt

views=[1200,2400,200,500]
sport =['cricket','football','badmintion','tennis']
plt.scatter(sport,views)
plt.xlabel('sports')
plt.ylabel('views in millions')
plt.title('viewership')
plt.show()

histogram
---------
import matplotlib.pyplot as plt

views=[1200,2400,200,500]
plt.hist(views)
plt.title('viewership')
plt.xlabel('views')
plt.ylabel('frequency')

plt.show()

boxplot
-------
import matplotlib.pyplot as plt

views=[1200,2400,200,500]
plt.boxplot(views)
plt.title('viewership')
plt.show()

'''