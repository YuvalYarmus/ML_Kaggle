from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

regressor = LinearRegression()

# https://www.kaggle.com/altavish/boston-housing-dataset/discussion/190403
# There are 14 attributes in each case of the dataset. They are:
# CRIM - per capita crime rate by town
# ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
# INDUS - proportion of non-retail business acres per town.
# CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
# NOX - nitric oxides concentration (parts per 10 million)
# RM - average number of rooms per dwelling
# AGE - proportion of owner-occupied units built prior to 1940
# DIS - weighted distances to five Boston employment centres
# RAD - index of accessibility to radial highways
# TAX - full-value property-tax rate per $10,000
# PTRATIO - pupil-teacher ratio by town
# B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# LSTAT - % lower status of the population
# MEDV - Median value of owner-occupied homes in $1000's


data = pd.read_csv("HousingData.csv")

# visualise the data
# sns.pairplot(data)
# plt.show()

# ratios
print("\nnumeric slope visualisation:")
print(data.corr())

# more plots
# fig, axes = plt.subplots(7, 2, figsize=(12,12))
# for i , feature in enumerate(data.columns): 
#     if i > 6:
#         i -= 7
#         j = 1
#     else: j = 0
#     print(f"{feature} : {data[feature]}")
#     sns.histplot(data[feature], ax=axes[i, j])
# plt.tight_layout()
# plt.show()

# we can see in the graph of each attribute:
# almost all houses have 5-8 rooms
# most houses are over 100 years old
# there are a lot of lage black populations
# most houses belong to lower status populations
# most houses arent far from the five Boston employment centres
# most houses dont have a lake nearby

# some are really really not normally distributed
# dont think we need zn, chas


# fig, axes = plt.subplots(7, 2, figsize=(12,12))
# for i , feature in enumerate(X.columns): 
#     if i > 5:
#         i -= 6
#         j = 1
#     else: j = 0
#     sns.regplot(x=data[feature], y=data["MEDV"] ,ax=axes[i, j])
# plt.tight_layout()
# plt.show()



# print(data.dropna().shape) 
# we got Nan

print(data[data.isna().any(axis=1)])
# we see now that most of the nans are in chas and lstat
# if lake proximity isnt true its probably false
data.CHAS.fillna(0, inplace=True)
# now we check how many nans are for the lstat to check if we can just delete it
print(f"lstat nan {len(data[data.LSTAT.isna()])}")
# only 20 - therefore we deleted
data = data[~ data.LSTAT.isna()]
print(f"lstat nan {len(data[data.LSTAT.isna()])}")
print(f"data size {data.shape}")
# actually just delete all of them
data = data[~ data.isna().any(axis=1)]
print(f"data size {data.shape}")


# making an x and y for the graph
X = data[["CRIM", "INDUS", "NOX", "RM", "AGE", "DIS",
 "RAD", "TAX", "PTRATIO", "B", "LSTAT"]]

Y = data["MEDV"]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=50)

# fit a linear line based the train group
regressor.fit(X_train, Y_train)

# the y values that match the x values from the test group based on our linear fit
Y_pred = regressor.predict(X_test)

# the plot between our predicted y values and the actual y values
sns.regplot(x=Y_test, y=Y_pred)
plt.show()

# a numeric value to how accurate the approximation is using rmse
# mse is the average of the squared errors
# r is their squared root
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
print(f"\nrmse: {rmse}\n")


# creating a data frame which shows the ratios between the values
data_frame = pd.DataFrame(data=["CRIM", "INDUS", "NOX", "RM", "AGE", "DIS",
"RAD", "TAX", "PTRATIO", "B", "LSTAT"],
index=regressor.coef_, columns=["feature"])
print(f"\npredicted ratios:\n{data_frame}\n")