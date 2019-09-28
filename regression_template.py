# regression template

# polynomial linear regression 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

"""from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
"""

"""from sklearn.preprocessing import StandardScaler 
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test) 
"""
#prediction based on polynomial regression
y_pred=regressor.predict(6.5)

#visualising polynomial regression results
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title("Truth or Bluff(Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#visualising polynomial regression results(for higher resolution and smoother curve)
x_grid=np.arange(min(x),max(x),0.1)
x_grid=x_grid.reshape((len(x_grid)),1)
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title("Truth or Bluff(Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()



