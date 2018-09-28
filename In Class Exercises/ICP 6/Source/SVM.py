from scipy.interpolate import rbf
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plot
from sklearn import metrics
iris = load_iris()

X = iris.data
Y = iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                            test_size=0.80, random_state=0)
#we compare gausian and svc using for loop and take accuracy values
for Model in [GaussianNB, LinearSVC]:
    clf = Model().fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    print('%s: %s' %
          (Model.__name__, metrics.f1_score(Y_test, y_pred, average="macro")))


    '''The biggest difference between the models you're building from a "features" point of view is that Naive Bayes treats them as independent,
       whereas SVM looks at the interactions between them to a certain degree,
       as long as you're using a non-linear kernel (Gaussian, rbf, poly etc.).
       So if you have interactions, and, given your problem, you most likely do, an SVM will be better at capturing those,
       hence better at the classification task you want.'''