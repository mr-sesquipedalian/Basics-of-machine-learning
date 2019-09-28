#hierarchial clustering


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values

#using dendrgram to find the number of clusters
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()

#fitting hierarchial clustering to mall dataset
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(x)

#visualising the clusters
plt.scatter(x[y_hc==0,0],x[y_hc==0,1],s=100,c='red',ec='black',label='careful')
plt.scatter(x[y_hc==1,0],x[y_hc==1,1],s=100,c='blue',ec='black',label='standard')
plt.scatter(x[y_hc==2,0],x[y_hc==2,1],s=100,c='green',ec='black',label='target')
plt.scatter(x[y_hc==3,0],x[y_hc==3,1],s=100,c='cyan',ec='black',label='careless')
plt.scatter(x[y_hc==4,0],x[y_hc==4,1],s=100,c='magenta',ec='black',label='sensible')
plt.title('Clusters of customers')
plt.xlabel('anuual income')
plt.ylabel('spending score')
plt.legend()
plt.show()


