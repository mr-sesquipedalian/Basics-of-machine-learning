# Random selection

#Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importing dataset
dataset=pd.read_csv('Ads_CTR_Optimisation.csv')

#implementing random selection
import random
n=10000
d=10
ads_selected=[]
total_reward=0
for i in range(0,n):
    ad=random.randrange(d)
    ads_selected.append(ad)
    reward=dataset.values[i,ad]
    total_reward=total_reward+reward
    
#Viusalising result-Histogram
plt.hist(ads_selected,ec='black')
plt.title('Histogram of ADS selection')
plt.xlabel('AD Number')
plt.ylabel('No. of times add selected')
plt.show()
    
