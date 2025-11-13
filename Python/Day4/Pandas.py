#Made By Punit

=================== x x x x x x x x ===================

#PANDAS

=================== x x x x x x x x ===================

#To Install Pandas in VS Code

#pip install pandas
#or
#python -m pip install pandas
#pip --version

=================== x x x x x x x x ===================

import pandas as pd

data=[10,20,30,40]
s=pd.Series(data)

print(s)

=================== x x x x x x x x ===================

import pandas as pd

data = {
    'name' : ['virat','ayush','nitesh','yash'],
    'age' : [21,23,18,12],
    'marks' : [91,90,89,88]
}

df= pd.DataFrame(data)
print(df)
print(pd.__version__)

=================== x x x x x x x x ===================

import pandas as pd

Data = [34,67,45]
y=pd.Series(Data)
print(y)

=================== x x x x x x x x ===================

#Series

import pandas as pd
a=[1,7,2]
myvar = pd.Series(a)
#myvar = pd.Series(a, index=['x','y','z'])
print(myvar["y"])
print(myvar)

=================== x x x x x x x x ===================

import pandas as pd
calories={"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

=================== x x x x x x x x ===================

#print(df.head()) # For Top 5 Data in Data Frame
#print(df.tail()) # For Last 5 Data in Data Frame
#print(df.info()) # To Check the Object Type

=================== x x x x x x x x ===================

#Q1 Create a pndas series from a dictionary:
# {"math":90,"science":85,"english":78}
# print the series
# access the marks for science
# show its .dtype amd .shape

=================== x x x x x x x x ===================

import pandas as pd
marks={"math":89,"science":45,"sst":67}
e=pd.Series(marks)

print(e)

print(e[1])

=================== x x x x x x x x ===================

#Made By Punit
