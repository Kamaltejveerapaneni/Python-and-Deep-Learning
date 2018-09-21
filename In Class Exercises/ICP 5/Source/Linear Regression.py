import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print(pd._version)
# x = np.array([0,1,2,3,4,5,6,7,8,9])
# y = np.array([1,3,2,5,7,8,8,9,10,12])
dataframe = pd.read_excel('C:\\Users\kamal\PycharmProjects\icp 5\SimpleLinear Regression.xls')


# print(dataframe.head[14])
x=dataframe.X
y=dataframe.Y

 #mean value of x and y
meanOfX = sum(x)/len(x)
meanOfy = sum(y)/len(y)

#calculating slope
slope = np.sum((x - meanOfX)*(y - meanOfy))/np.sum(np.square(x-meanOfX))
#calculating intercept
intercept = meanOfy - (slope * meanOfX)
#y output
yOutput = (slope * x) + intercept

#change default fig size
plt.figure(figsize=(10,10))
plt.scatter(x,y)
plt.plot(x,y,"ro")  # plotting the line made by linear regression
plt.plot(x, yOutput, color="red",linewidth=4)
plt.xlabel("X:national unemployment rate for adult males",fontsize=20)
plt.ylabel("Y:national unemployment rate for adult females",fontsize=20)

#font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.show()