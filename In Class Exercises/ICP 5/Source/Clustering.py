
#importing the required libraries:
import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

#prepare the data that we want to cluster
#We create a numpy array of data points because
# the Scikit-Learn library can work with numpy array type data inputs without requiring any preprocessing.
X = np.array([[1,1],
     [1.5,2.0],
     [3.0,4.0],
     [5.0,7.0],
     [3.5,5.0],
     [4.5,5.0],
     ])
#Visualize the Data
plt.scatter(X[:,0],X[:,1], label='True Position')

# you create a KMeans object and pass it 2 as value for n_clusters parameter.
# Next, you simply have to call the fit method
kmeans = KMeans(n_clusters=2)

#let's see what centroid values the algorithm generated for the final clusters. Type:
kmeans.fit(X)
print(kmeans.cluster_centers_)
#labels = kmeans.predict(X)

#centroids = kmeans.cluster_centers

#print(centroids)
#The output is a one dimensional array of 6 elements corresponding to the clusters assigned to our 6 data points
print(kmeans.labels_)

#print("sklearn")
#we will plot the data along with their assigned label so that we can distinguish between the clusters.
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')




#plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
#plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')


plt.show()

