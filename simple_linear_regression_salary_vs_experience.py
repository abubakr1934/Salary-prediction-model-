# -*- coding: utf-8 -*-
"""simple_linear_regression-Salary vs experience.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iVggPaCQc6xxqZJgqH9HfEUL1VoX7gq

# Simple Linear Regression

## Importing the libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Importing the dataset"""

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(X_train,y_train)# x train contains the independent variable and y train contains the dependent variables for the output of regression

"""## Predicting the Test set results"""

hello=regressor.predict(X_test)#passing the test set

"""## Visualising the Training set results"""

plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')#x train values pe what predicted salary is given by the regressor function
plt.title('salary versus experience')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()

"""## Visualising the Test set results"""

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()



