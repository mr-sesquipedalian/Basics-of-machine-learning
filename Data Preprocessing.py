import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

#importing dataset
dataset=pd.read_csv("Data.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

#categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0],dtype=np.int64)
x=onehotencoder.fit_transform(x).toarray()

labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)

#splitting the dataset into training amd test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler 
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)
