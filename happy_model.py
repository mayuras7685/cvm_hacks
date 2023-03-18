# Importing the required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
# Reading the dataset
data = pd.read_csv('data/happy.csv')
 
# Seperating the target and features
# target ->y, features -> X
y = data['Percentage']
X = data.drop(columns='Percentage', axis=1)
 
# Splitting into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
 
# Making the model
lr = LinearRegression()
lr.fit(X_train, y_train)
 
# Predicting the output
y_pred = lr.predict(X_test)
 
# Saving the model
import joblib
 
joblib.dump(lr, "lr_model.sav")