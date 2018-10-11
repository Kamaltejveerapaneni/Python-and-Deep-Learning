from sklearn.naive_bayes import GaussianNB
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


daibetesDS=datasets.load_diabetes()
X=daibetesDS.data
Y=daibetesDS.target


model_1= GaussianNB()
model_1.fit(daibetesDS.data, daibetesDS.target)

X_train, X_test, Y_train, Y_test = train_test_split(daibetesDS.data, daibetesDS.target, test_size=0.4, random_state=1)

model_1.fit(X_train, Y_train)

# Training the Model on Testing Set
Y_predicted = model_1.predict(X_test)

# Evaluating the Model based on Testing Part
print("GM accuracy", metrics.accuracy_score(Y_test, Y_predicted) * 100)

#plotting each category

# https://seaborn.pydata.org/tutorial/categorical.html

#categories in dataset= age,sex,bmi,bp,s1,s2,s3,s4,s5,s6,y
#https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html
dbdata = pd.read_table('diabetes.txt')

plot = plt.figure(figsize=(8, 4))
plot.add_subplot(1, 1, 1)
cat = sns.countplot(dbdata['AGE'], label="Count") #using seaborn library
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="left", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['SEX'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="left", fontsize=5)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['BMI'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=7)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['BP'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=5)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['S1'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['S2'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['S3'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['S4'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['S5'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['S6'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()

cat = sns.countplot(dbdata['Y'], label="Count")
cat.set_xticklabels(cat.get_xticklabels(), rotation=40, ha="right", fontsize=6)
plt.tight_layout()
plt.show()