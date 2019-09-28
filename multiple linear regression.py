import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

#avoiding dummy variables
x=x[:,1:]


#splitting the dataset into training amd test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#feature scaling
"""
from sklearn.preprocessing import StandardScaler 
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)
"""
#fitting multiple linear regression in training set
from sklearn.linear_model import LinearRegression 
regressor=LinearRegression()
regressor.fit(x_train,y_train)

#predicting the test set results
y_pred=regressor.predict(x_test) 
    
#building the optimal model using backward elimination
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
import statsmodels.formula.api as smf
x_opt=x[:,[0,1,2,3,4,5]]
regressor_OLS = smf.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
x_opt=x[:,[0,1,3,4,5]]
regressor_OLS = smf.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
x_opt=x[:,[0,3,4,5]]
regressor_OLS = smf.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
x_opt=x[:,[0,3,5]]
regressor_OLS = smf.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()
x_opt=x[:,[0,3]]
regressor_OLS = smf.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()







