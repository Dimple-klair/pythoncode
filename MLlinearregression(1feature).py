# import below 3 packages:-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model
# we can import sklearn whole but its not a good practice.so import what you want from it
# we can import datasets from UCIML REPOSITORY/KAGGLE ETC
# sklearn provides us preexisting datasets.so import from there in our python
# we are importing/loading diabetic dataset
diabetes = datasets.load_diabetes()  # import this dataset
# print(diabetes.keys()) #telling what's inside this dataset(all keys)
# print(diabetes.data) # SHOWS NUMPY ARRAYS
# print(diabetes.DESCR) #TELLS ABOUT DATASET/TARGET/FEATURES

# NOW FIT LINE/PLOT/DRAW LINE WITH MATPLOTLIB:-
# WITH 1 FEATURE ONLY[2nd index]:-
diabetes_X = diabetes.data[:, np.newaxis, 2]
# print(diabetes_x) #shows arrays of arrays/list of lists /put 2nd index in a column

# slicing/SPLITING DATA
diabetes_X_train = diabetes_X[:-30]  # taking last 30 data for train
diabetes_X_test = diabetes_X[-30:]  # taking first 30 and all

# GIVING Y labels for train /test:-
diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-30:]

# X-AXIS=FEATURES(INPUT) / Y-AXIS=LABEL(OUTPUT)
# NOW DRAW A LINEAR LINE WITH THE HELP OF- FEAT AND LABEL
# AND WITH THAT LIN. LINE WE PREDICT OTHER POINTS./WE PUT VALUE OF COMING FEAT. AND PREDICT POINTS TO FIND LABEL.
# NOW CREATE A LINEAR MODEL WITH SKLE LEARN
# we already import this lin.modelfrom sklearn in 5th line.and feed it lin.regression.bec we use lin.regression method.
model = linear_model.LinearRegression()

# NOW FIT DATA means-WITH HELP OF DATA WE MAKE A LINE AND THAT LINE WILL SAVE IN LIN MODEL.
# first train the data./train means -LEARNING TO GET THAT LINE.
model.fit(diabetes_X_train, diabetes_Y_train)
# AFTER GETTING LINE FROM TRAINING WE TEST THE LINE(WHETHER RIGHT OR WRONG)


####### MODEL ALREADY MADE IN LINE (34)##########


# NOW TEST THE MODEL(TESTING PART)
# Y IS LABEL. X IS FEAT..USING X WE PREDICT AND FIND Y(LABEL)
diabetes_Y_predicted = model.predict(diabetes_X_test)


# NOW JUST BRING DATA AND FEED HERE.BASICALLY WE MUST KNOW (NUMPY)TO FEED DATA IN ARRAY.
# use formula:-
# NOW FIND OUT MEAN SQUARED ERROR(MSE)=average of SSE
# 2 parameters-test(y-test=actual) & predict
print("MSE is: ", mean_squared_error(diabetes_Y_test, diabetes_Y_predicted))


# NOW FIND WEIGHT(10 theta) (BEFORE PLOT)
print("weight:", model.coef_)  # coefficient(10 theta)
print("intercept:", model.intercept_)  # intercept(B IN GRAPH)


# NOW PLOT FEATURES AND LABEL:-
plt.scatter(diabetes_X_test, diabetes_Y_test)
# make a line between scattered points./AND MINIZING OUR MSE
plt.plot(diabetes_X_test, diabetes_Y_predicted)
plt.show()  # THIS SHOWS US ALL 30 VALUES WE TOOK FOR TESTING
