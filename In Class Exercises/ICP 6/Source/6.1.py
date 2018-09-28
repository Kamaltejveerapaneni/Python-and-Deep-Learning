from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plot
from sklearn import metrics
#Scikit-learn has a very straightforward set of data on these iris species. The data consist of the following:
'''
Features in the Iris dataset:
sepal length (cm) sepal width (cm) petal length (cm) petal width (cm)
Target classes to predict:
Setosa Versicolour Virginica
scikit-learn embeds a copy of the iris CSV file along with a function to load it into numpy arrays:'''
iris = load_iris()
print(iris.data.shape)
n_samples,n_features = iris.data.shape

#The features of each sample flower are stored in the data attribute of the dataset:
print(iris.data.shape)
n_samples,n_features = iris.data.shape

print(n_samples)
print(n_features)
print(iris.data[0])
#The information about the class of each sample is stored in the target attribute of the dataset:
print(iris.target.shape)
print(iris.target)
#he names of the classes are stored in the last attribute, namely target_names:
print(iris.target_names)


X=iris.data
Y=iris.target

# split the data into training and validation sets
#X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)





# splitting data and target into training and testing sets
"""http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html"""
"""https://www.scipy-lectures.org/packages/scikit-learn/index.html"""
# If int, random_state is the seed used by the random number generator
# If float, test_size represent the proportion of the dataset to include in the test split [Default: 0.75]
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.75, random_state=0)

# train the model
clf = GaussianNB()
clf.fit(X_train, Y_train)


# use the model to predict the labels of the test data
predicted = clf.predict(X_test)
expected = Y_test
print(predicted)

print(expected)
plot.plot(expected, predicted)
plot.show()

'''Cross-validation consists in repetively splitting the data in pairs of train and test sets, called ‘folds’. 
Scikit-learn comes with a function to automatically compute score on all these folds.
 Here we do KFold with k=5.'''
clf = KNeighborsClassifier()
from sklearn.model_selection import cross_val_score
cvs = cross_val_score(clf, X, Y, cv=5)
print("cvs",cvs)

print(metrics.classification_report(expected, predicted))
# confusion_matrix - To evaluate Accuracy of classification
print(metrics.confusion_matrix(expected, predicted))


# Training the Model on Training Set
clf.fit(X_train, Y_train)

# Training the Model on Testing Set
Y_predicted = clf.predict(X_test)

# Evaluating the Model based on Testing Part
print("Gaussian Model Accuracy is ", metrics.accuracy_score(Y_test, Y_predicted) * 100)