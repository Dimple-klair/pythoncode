# doing with 1 feature only(petal width)
#----WE ARE TRAINING LOGISTIC REGRESSION TO PREDICT WHETHER A FLOWER IS IRIS VERGINICA OR NOT------#
from sklearn import datasets
import numpy as np  # bec, log. reg. class. donot understand binary lang.
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris = datasets.load_iris()
# print(iris['data'])

# now storing data and target in 1 var.(x):-
# SLICING (taking only 1 feture)(3rd index-petal width)
x = iris['data'][:, 3:]
# print(x)


# MAKING BINARY CLASSIFIER(true/false):-
# y = (iris['target'] == 2)  # then true
# print(y)

y = (iris['target'] == 2).astype(np.int)
# print(y)

# NOW TO TRIAN LOG.CLASS. SO IMPORT LINEAR_MODEL LOG.REG.
clf = LogisticRegression()
clf.fit(x, y)
pred = clf.predict(([[2.0]]))  # give any 1 feature to predict
# print(pred)
# so our model is doing predictions above


#             NOW PLOT(VISUALIZE OUR CLASS.)
# JUST TO MAKE A - (S GRAPH.....in logistic regression)
# NOW TAKING NEW FEATURE IN A VAR(X_NEW)
# Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
# petal width ki 100 values le li hai humne bet.0-5
x_new = np.linspace(0, 5, 100).reshape(-1, 1)
# print(x_new)
y_prob = clf.predict_proba(x_new)
# print(y_prob)

# NOW PLOT(VISUALIZE OUR CLASS.)
plt.plot(x_new, y_prob[:, 1])  # this gives 1 row only
plt.show()
