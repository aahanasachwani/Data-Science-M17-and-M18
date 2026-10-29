import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
file = files.upload()

data = pd.read_csv('Pokemon Data.csv')
data.head()

data['Type 2'].fillna(value='None',inplace=True)
data.isnull().sum()

data['Type 1'].value_counts().plot.bar()
data['Type 2'].value_counts().plot.bar()
data['Legendary'].value_counts().plot.bar()

data['Type 1'].unique()
data['Type 2'].unique()

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
data['Legendary'] = lb.fit_transform(data['Legendary'])

data.head()

data.drop('Name', axis=1, inplace=True)

data = pd.get_dummies(data)

data.shape

from sklearn.metrics import accuracy_score
ypred1 = LogReg.predict(X_test)
accuracy_score(y_test,ypred1)

from sklearn.neighbors import KNeighborsClassifier
error_rates = []

for a in range(1, 40):
    k = a
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(y_test - preds))

plt.figure(figsize=(10, 7))
plt.plot(range(1,40),error_rates,color='blue', linestyle='dashed', marker='o',
markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

knn_model = KNeighborsClassifier(n_neighbors=8)
knn_model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_predict = knn_model.predict(X_test)
accuracy_score(y_test, y_predict)

from sklearn.tree import DecisionTreeClassifier
clf_model = DecisionTreeClassifier()
clf_model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_predict = clf_model.predict(X_test)
accuracy_score(y_test, y_predict)