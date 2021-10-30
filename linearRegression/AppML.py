from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

regressor = LinearRegression()

# can be used in python notebooks according to:
# https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up
# %matplotlib inline

data = pd.read_csv("data.csv")

# the head function shows the first n rows from the csv file
print("\ndata head:")
print(data.head(10))

# the describe function shows the numeric values in the csv file
print("\ndata description:")
print(data.describe())

# the shape function shows how many rows and attributes are in the csv file
# print(data.shape())


# visualise the data:
# sns.pairplot(data)
# plt.show()

# a more numeric way to visualise the slopes/ratios
print("\nnumeric slope visualisation:")
print(data.corr())

# heatmap
# sns.heatmap(data.corr())
# plt.show()

# making an x and y for the graph
X = data[["Avg. Session Length", "Time on Website", "Time on App", "Length of Membership"]]
# print(X.head(5))

Y = data["Yearly Amount Spent"]
# print(Y.head(5))

# split randomly (or by a random state) to 2 groups: train and test
# one will be used to design the linear graph and the other to test it
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# fit a linear line based the train group
regressor.fit(X_train, Y_train)

# print("the test:")
# print(X_test)
# print(Y_test)

# the y values that match the x values from the test group based on our linear fit
Y_pred = regressor.predict(X_test)
# print(Y_pred)

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
data_frame = pd.DataFrame(data=["Avg. Session Length", "Time on Website", "Time on App", "Length of Membership"],
index=regressor.coef_, columns=["feature"])
print(f"\npredicted ratios: {data_frame}\n")