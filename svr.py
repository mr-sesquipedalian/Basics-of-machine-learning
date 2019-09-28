# svr

# polynomial linear regression 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2:3].values


#test and training datset
"""from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
"""
#feature scaling
from sklearn.preprocessing import StandardScaler 
sc_x=StandardScaler()
sc_y=StandardScaler()
x=sc_x.fit_transform(x)
y=sc_y.fit_transform(y)

#fitting SVR to dataset
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(x,y)


#prediction based on polynomial regression
y_pred=sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[ 6.5]]))))

#visualising polynomial regression results
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title("Truth or Bluff(Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#visualising polynomial regression results(for higher resolution and smoother curve)
x_grid=np.arange(min(x),max(x),0.1)
x_grid-x_grid.reshape((len(x_grid)),1)
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title("Truth or Bluff(SVR)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()