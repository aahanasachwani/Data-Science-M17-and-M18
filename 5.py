# Commented out IPython magic to ensure Python compatibility.
#Importing requirede libraries

import pandas as pd
from matplotlib import pyplot as plt
from google.colab import files
# %matplotlib inline

#Importing Dataset required

uploaded = files.upload()
df = pd.read_csv("insurance_data.csv")
df.head()

#Ploting the dataset

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')

#Spliting the training Values usijg sklearn

from sklearn.model_selection import train_test_split

#Defining the Training and Testing Variables

X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

X_test

#Using Logistic Regression Algorithmn

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#Fitting the model

model.fit(X_train, y_train)

X_test

#Predicting the Y

y_predicted = model.predict(X_test)

model.predict_proba(X_test)

#Testing model

model.score(X_test,y_test)

y_predicted

X_test

model.coef_

model.intercept_

import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def prediction_function(age):
    z = 0.042 * age - 1.53 # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53
    y = sigmoid(z)
    return y

age = 35
prediction_function(age)

age = 43
prediction_function(age)

#0.485 is more than 0.5 which means person with 43 will buy the insurance

