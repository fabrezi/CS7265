import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#upload data
data = pd.read_csv("C:\\Users\\farid-PC\\Desktop\\class\\CS7265_BIG_DATA\\HW3\\housing_training.csv", header=None)
# CRIM: crime rate by town per capita || ZN: land zoned for lots(sq.ft) || INDUS: non-retail land(sq.ft) || CHAS: 1 - bound river 0 - null || NOX: nitro oxide concentration(per 10 million)
# RM: avg of rooms || age:  || DIS: weight mean of distance || RAD: index of accessibiltiy to radial highway ||  TAX: per 10000 || PTRATIO: pupil teacher ratio || B: black in town ||
# LSTAT: percent || MEDV (target variable): median value of the owner occupied homes in 1000
# Predict: the cost of the house
data.rename(columns= {0: 'CRIM', 1: 'ZN', 2: 'INDUS', 3: 'CHAS', 4: 'NOX', 5: 'RM', 6: 'AGE', 7: 'DIS', 8: 'RAD', 9: 'TAX', 10: 'PTRATIO', 11: 'B', 12: 'LSTAT', 13: 'MEDV'}, inplace=True)
#print(data)
print(data.head())

print('\n')


#correlation matrix
#corr_matrix = data.corr().round(2)
#sns.heatmap(data=corr_matrix, annot=True, fmt="g", cmap='viridis')
#plt.show()

#train the classifier

#test_method
#def plotFeatures(col_list):
  #  plt.figure(figsize=(10,14))
   # i=0
    #print(len(col_list))
    #for col in col_list:
     #   i += 1
      #  plt.subplot(7,2,i)
       # plt.plot(data[col], data["MEDV"], marker='.', linestyle='none')
        #plt.title(title%(col))
        #plt.tight_layout()
#colnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NPX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
#plotFeatures(colnames)
