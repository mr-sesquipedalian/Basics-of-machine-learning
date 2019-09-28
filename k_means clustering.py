#k-means clustering

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importing dataset
dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values

#using elbow method to find number of clusters
from sklearn.cluster import KMeans
wcss=[]
l=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',n_init=10,max_iter=300,random_state=0)
    kmeans.fit(x)
    l.append(i)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11 ),wcss)
plt.xticks(l)
plt.grid()
plt.title('Elbow Method')
plt.xlabel('No. of clusters')
plt.ylabel('WCSS')
plt.show()

#elbow point is k=5
#predicing the cluster to given point
kmeans=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(x)

#visualising clusters
plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100, c='red', label='careful',ec='black')
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100, c='blue', label='balanced',ec='black')
plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=100, c='green', label='target',ec='black')
plt.scatter(x[y_kmeans==3,0],x[y_kmeans==3,1],s=100, c='cyan', label='careless',ec='black')
plt.scatter(x[y_kmeans==4,0],x[y_kmeans==4,1],s=100, c='magenta', label='sensible',ec='black')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroids',ec='black')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()



    