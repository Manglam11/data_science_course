import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# imported all the required libraries with their standard alias
dataset = pd.read_csv("Salary_Data.csv")
# imported the dataset locally from machine
x = dataset.iloc[:, :-1]
# splits the data into x and y. here in x let me tell you what i understand cause i alsays get confused in slicing. first : means all the rows. ',' is separating the rows and columns so next part will be going to realte with column. here : means from 0 to -1 but not inlude -1 so last column will not be included. (i think that is dependent var that's why we are separating it.
y = dataset.iloc[:, -1]
# here again : means all the rows than for col we just added -1 means very last col present in dataset ie dependent var
from sklearn.model_selection import train_test_split
# we imporint this means our datasize is enough large to spplit it into test and training data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
# we created 4 var means train_test_split return 4 tuplse values. it is taking x and y data, test size is defined as 0.2 means the distribtion is 80 percent training 20 percent testing, random_state it is the seed set to a fix value so every time split happens same even for new users.
from sklearn.linear_model import LinearRegression
# this is our model class means engine from skleanr library and further linear_model

regressor = LinearRegression()
# we created object of our model
regressor.fit(x_train, y_train)
# using the boject we uses the fit function. it is like the power button which acutally runs our engine with data.
y_pred = regressor.predict(x_test)
# now we are telling hey you run our test data you now know pattarn now predict for new data i know result already but i want to evaluate you.
comparision = pd.DataFrame({'Actual': y_test, 'Prediction': y_pred})
# we created our comparison dataframe
print(comparision)

plt.scatter(x_test, y_test, color='Red')
# 
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary of employee based on experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# validataion or future data

c_inter = regressor.intercept_
print(f'Intercept: {regressor.intercept_}')

m_coef = regressor.coef_
print(f'Coefficient: {regressor.coef_}')

y_12 = m_coef * 12 + c_inter
print(y_12)

y_20 = m_coef * 20 + c_inter
print(y_20)

bias_training = regressor.score(x_train, y_train)
print(bias_training)

variance_testing = regressor.score(x_test, y_test)
print(variance_testing)

# Lets implement stats to this model

dataset.mean()
dataset['Salary'].mean()
dataset['YearsExperience'].mean()

dataset.median()
dataset['Salary'].median()
dataset['YearsExperience'].median()

dataset.var()
dataset['Salary'].var()
dataset['YearsExperience'].var()

dataset.std()
dataset['Salary'].std()
dataset['YearsExperience'].std()

from scipy.stats import variation

variation(dataset.values)
variation(dataset['Salary'])
variation(dataset['YearsExperience'])

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])
dataset['Salary'].corr(dataset['Salary'])

dataset.skew()

dataset.sem()

import scipy.stats as stats

dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])
stats.zscore(dataset['YearsExperience'])

# ANOVA

y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean) ** 2)
print(SSR)

y = y[0:6]
SSE = np.sum((y - y_pred) ** 2)
print(SSE)

mean_total = np.mean(dataset.values)
# here df.to_numpy()will convert pandas Dataframe to Nump
SST = np.sum((dataset.values - mean_total) ** 2)
print(SST)

r_square = 1 - (SSR / SST)
r_square

print(r_square)
print(bias_training)
print(variance_testing)

