import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data  # taking all data not 1 feature

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_Y_train)

# paas test data only during prediction time
diabetes_Y_predict = model.predict(diabetes_X_test)
print("MSE is: ", mean_squared_error(diabetes_Y_test, diabetes_Y_predict))
print('weight is: ', model.coef_)
print('intercept is: ', model.intercept_)
