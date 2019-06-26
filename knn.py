import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

##perform KNN on iris dataset

#upload data
data = pd.read_csv("C:\\Users\\farid-PC\\Desktop\\iris.csv")


#array
#X = np.array(data.loc[:, data.columns != 'LABEL'])
#Y = np.array(data['LABEL'])

X = np.array(data.iloc[:, 0:4])
Y = np.array(data['Label'])

#split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

#classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)

#prediction
pred = knn.predict(X_test)
print("accuracy:", accuracy_score(Y_test, pred)*100, "%")

#cross-validation
myList = list(range(1,25))
neighbors = list(filter(lambda x: x % 2 != 0, myList))
cv_scores = [] #list to hold cv scores

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=3)
    scores = cross_val_score(knn, X_train, Y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())


#misclassification error
MSE = [1 - x for x in cv_scores]

#plot
plt.plot(neighbors, MSE)
plt.xlabel("K")
plt.ylabel("ERROR")
plt.show()
