# USING CLASSIFIER ALGO for making ml model
# LOADING REQUIRED MODULES:-
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
# print(iris.DESCR) #THIS DESCRIBE 4 ATTRIBUTE/FEAT. AND 3LABELS(012)

# printing features and labels:-
features = iris.data
labels = iris.target
# printing(FEATURES AND LABELS) here only 1 feature with INDEX[0]
#print(features[0], labels[0])
# OUTPUT= [5.1 3.5 1.4 0.2] 0
# HERE TOTAL 4 FEAT. AND 0 IS LABEL / # 0 MEANS SATOSA FLOWER


# NOW TRAIN THE CLASSIFIER(K NEAREST CLASSIFIER):-(with data)
clf = KNeighborsClassifier()
# we made classifier now,
# now fit classifier:-
clf.fit(features, labels)

# NOW TAKE PREDICTIONS FROM IT:-
pred = clf.predict([[20, 12, 11, 14]])  # giving new features to predict/label
print(pred)
# OUTPUT= [5.1 3.5 1.4 0.2] 0 [2] # (2 MEANS VERGINICA)
# with new features our classifier(ALGO) predict new labels.
