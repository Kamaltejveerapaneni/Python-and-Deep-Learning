import statsmodels.api as sm
import numpy as np
import pandas as pd#pandas is a package commonly used to deal with data analysis
import scipy.stats as stats
#Since we are going to work on some plotting, we will import matplotlib like this:
import matplotlib.pyplot as plt


from scipy.stats import linregress
print(pd.__version__)
#read the excel data into dataframe
#The DataFrame represents tabular data, a bit like a spreadsheet.
#We can create a DataFrame in Pandas from a Python dictionary
dataframe = pd.read_excel("C:\\Users\kamal\PycharmProjects\icp 5\SimpleLinear Regression.xls")

print(dataframe.head(14))

x = dataframe.X#X values are assigned to x
y = dataframe.Y#Y values are assigned to y

#The linregress function is slightly different to the functions we’ve seen so far, because it returns an object with multiple values.
#In fact it returns the slope, intercept, rvalue, pvalue, and stderr (standard error).
# We can get hold of each of these values by using the dot notation:
# e.g. stats.slope, for example, much in the same way we can access our DataFrame attributes with dataframe.Height.

stats = linregress(x,y)

m = stats.slope
b = stats.intercept

#change default fig size
plt.figure(figsize=(10,10))
#Then we can plot them as a scatter chart by adding:
plt.plot(x,y)
#plotting the graph and setting the line width
plt.plot(x,m*x + b, color ="red", linewidth=6)

#Add x and y labels,and set their font size
plt.xlabel("X:national unemployment rate for adult males",fontsize=20)
plt.ylabel("Y: national unemployment rate for adult females",fontsize=20)

#font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)






#To make Python show the chart, we need to either save the figure, or show it in Spyder

plt.show()






