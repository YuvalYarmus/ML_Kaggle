import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('train.csv')

# Pclass: Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
# survival: Survival (0 = No; 1 = Yes)
# name: Name
# sex: Sex
# age: Age
# sibsp: Number of Siblings/Spouses Aboard
# parch: Number of Parents/Children Aboard
# ticket: Ticket Number
# fare: Passenger Fare (British pound)
# cabin: Cabin
# embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
# all according to:
# http://campus.lakeforest.edu/frank/FILES/MLFfiles/Bio150/Titanic/TitanicMETA.pdf


print(df.shape, end="\n\n")
print(df.head(), end="\n\n")
print(df.describe(), end="\n\n")
print(df.count(), end="\n\n")

# many missing values on cabin and age
# cabin is probably related to fare so prob shouldnt care about it that much

# sns.heatmap(df.isnull())
# plt.show()

# sns.pairplot(df)
# plt.show()

df['Sex'] = df.Sex.apply(lambda x: 1 if x=='female' else 0)
print(df.Sex, end="\n\n")

print(df.groupby('Survived').mean(), end="\n\n")

# survived_by_gender = df.pivot_table(values="Survived", index="Sex")
# sns.heatmap(survived_by_gender)
# plt.show()

# sns.countplot(data=df, x="Survived", hue="Sex")
# plt.show()


no_age_mean = df[df['Age'].isna()].mean(numeric_only=True)
age_mean = df[df['Age'].notna()].mean(numeric_only=True)
print(f"no_age_mean:\n{no_age_mean}" , end="\n\n")
print(f"age_mean:\n{age_mean}", end="\n\n")
print(f"diff:\n{no_age_mean - age_mean}" , end="\n\n")

# we can see that passengers with no recorded age, compre to those who had recorded age, had:
# lower id numbers
# lower survival rate
# a higher pclass
# mostly male
# had more siblings or spouses
# had less children or parents
# had a lower fare

# Therefore it is probably meaningfull wether one has a recorded age or not

df['hasAge'] = df['Age'].notna().astype(int)

print(df[df['Age'].isna()].hasAge.head(), end="\n\n")
print(df[df['Age'].notna()].hasAge.head(), end="\n\n")

# now we would also like to try and fill the age which are nan with an
# age that the difference between its survival rate and the general survival rate
# is as close as possible to the difference in survival rate between
# passengeres with and without a registered age (which we saw is: -0.112377)



age_buffer = 2
start_age = 10
stop_age = 25
ages = np.arange(start_age, stop_age, age_buffer).tolist()
wanted_diff = -0.112377
min_diff = 99999
fill_Age = -1
print(f"ages: {ages}" , end="\n\n")
for age in ages:
    age_group = df[(df.Age < age + age_buffer) & (df.Age > age - age_buffer)]
    survival_rate = age_group.Survived.mean()
    survival_diff = survival_rate - df.Survived.mean()
    print(f"age: {age}\nsurvival_rate: {survival_rate}\nsurvival_diff: {survival_diff}", end="\n\n")
    if (survival_diff- wanted_diff < min_diff):
        min = survival_diff
        fill_Age = age

print(f"fill age is: {fill_Age}" , end="\n\n")
df.Age.fillna(fill_Age, inplace=True)

embarked = pd.get_dummies(df.Embarked)
df = pd.concat([df, embarked], axis=1)

print(df.describe(), end="\n\n")
print(df.info(), end="\n\n")

features = ['Pclass', 'Sex', 'hasAge', 'Age', 'SibSp', 'Parch', 'Fare', 'C', 'Q', 'S']
X = df[features]
Y = df['Survived']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=50)

regressor = LogisticRegression(solver='lbfgs', max_iter=820)

# fit a linear line based the train group
print("ABOUT TO FIT")
regressor.fit(X_train, Y_train)

# the y values that match the x values from the test group based on our linear fit
print('ABOUT TO PREDICT')
Y_pred = regressor.predict(X_test)

conf_mat = confusion_matrix(Y_test, Y_pred)
# tn, fp, fn, tp
print(f"\nconf_mat\n")
# in our case:
# we said 89 would die and they died
# we said 12 would live and they died
# we said 24 would die and they lived
# we said 54 would live and they lived
tn = 89
fp = 12
fn = 24
tp = 54

percision = (tp + tn) / len(Y_pred)
recall = tp / (tp + fn)

print(f"precision: {percision}\nrecall: {recall}\n")
# precision: 0.7988826815642458
# recall: 0.6923076923076923
# not bad I think

f1 = 2 * (percision * recall) / (percision + recall)
print(f"f1 score: {f1}")
# f1 score: 0.7417867435158502
