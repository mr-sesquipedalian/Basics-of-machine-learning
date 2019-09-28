import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv("50_Startups.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values

#categorical data encoding and dummy variables
from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
x[:,3]=labelencoder_x.fit_transform(x[:,3])

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[3],dtype=np.float64)
x=onehotencoder.fit_transform(x).toarray()

x2=x[:,3]

from sklearn.model_selection import train_test_split
x2_train,x2_test,y_train,y_test=train_test_split(x2,y,test_size=0.2,random_state=0)

#feature scaling
"""from sklearn.preprocessing import StandardScaler 
sc_x2=StandardScaler()
x2_train=sc_x2.fit_transform(x2_train)
x2_test=sc_x.transform(x2_test)
sc_y=StandardScaler()
y_train=sc_y.fit_transform(y_train)"""

x2_train=x2_train.reshape(-1,1)
y_train=y_train.reshape(-1,1)
x2_test=x2_test.reshape(-1,1)
y_test=y_test.reshape(-1,1)

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x2_train,y_train)

#predicting the test set results
y_pred=regressor.predict(x2_test)

#plotting training results
plt.scatter(x2_train,y_train,color='red')
plt.plot(x2_train,regressor.predict(x2_train),color='blue')
plt.show()

#plotting test results
plt.scatter(x2_test,y_test,color='red')
plt.plot(x2_test,regressor.predict(x2_test),color='blue')
plt.show()


