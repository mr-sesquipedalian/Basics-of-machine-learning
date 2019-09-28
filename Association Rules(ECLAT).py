#ECLAT

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv('Market_Basket_Optimisation.csv', header=None)

#making list of lists
transactions=[]
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
#training apriori on datasets
from apyori import apriori 
rules=apriori(transactions, min_support=0.003)

#visualising the result
results=list(rules)
