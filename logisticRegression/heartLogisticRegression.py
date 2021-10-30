import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# Heart Disease Data Dictionary
# Taken from: https://www.kaggle.com/ronitf/heart-disease-uci/discussion/273496

# The following are the features we'll use to predict 
# our target variable (heart disease or no heart disease).

# 1. age - age in years
# 2. sex - (1 = male; 0 = female)
# 3. cp - chest pain type
#       0: Typical angina: chest pain related decrease blood supply to the heart
#       1: Atypical angina: chest pain not related to heart
#       2: Non-anginal pain: typically esophageal spasms (non heart related)
#       3: Asymptomatic: chest pain not showing signs of disease
# 4. trestbps - resting blood pressure (in mm Hg on admission to the hospital)
#       anything above 130-140 is typically cause for concern
# 5. chol - serum cholestoral in mg/dl
#       serum = LDL + HDL + .2 * triglycerides
#       above 200 is cause for concern
# 6. fbs - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
#       '>126' mg/dL signals diabetes
# 7. restecg - resting electrocardiographic results
#       0: Nothing to note
#       1: ST-T Wave abnormality
#        can range from mild symptoms to severe problems
#        signals non-normal heart beat
#       2: Possible or definite left ventricular hypertrophy
#        Enlarged heart's main pumping chamber
# 8. thalach - maximum heart rate achieved
# 9. exang - exercise induced angina (1 = yes; 0 = no)
# 10. oldpeak - ST depression induced by exercise relative to rest
#       looks at stress of heart during excercise
#       unhealthy heart will stress more
# 11. slope - the slope of the peak exercise ST segment
#       0: Upsloping: better heart rate with excercise (uncommon)
#       1: Flatsloping: minimal change (typical healthy heart)
#       2: Downslopins: signs of unhealthy heart
# 12. ca - number of major vessels (0-3) colored by flourosopy
#       colored vessel means the doctor can see the blood passing through
#       the more blood movement the better (no clots)
# 13. thal - thalium stress result
#       1,3: normal
#       6: fixed defect: used to be defect but ok now
#       7: reversable defect: no proper blood movement when excercising
# 14. target - have disease or not (1=yes, 0=no) (= the predicted attribute)


df = pd.read_csv('heart.csv')

print(f"shape: {df.shape}", end="\n\n")
print(f"head:\n{df.head()}", end="\n\n")
print(f"describe:\n{df.describe()}", end="\n\n")
print(f"count:\n{df.count()}", end="\n\n")
print(f"\ninfo:", end="\n\n")
df.info()


# sns.pairplot(df)
# plt.show()

# sns.violinplot(data=df, x="sex", y="target")
# plt.show()

# sns.violinplot(data=df, x="target", y="sex")
# plt.show()

# sns.countplot(data=df, x="sex", hue="target")
# plt.show()

print(df.groupby('target').mean(), end="\n\n")
print(df.groupby('target').restecg.mean(), end="\n\n")

#               age       sex        cp    trestbps        chol       fbs  restecg     thalach     exang   oldpeak     slope        ca      thal
# target                                                                                                                                 
# 0       56.601449  0.826087  0.478261  134.398551  251.086957  0.159420  0.449275  139.101449  0.550725  1.585507  1.166667  1.166667  2.543478
# 1       52.496970  0.563636  1.375758  129.303030  242.230303  0.139394  0.593939  158.466667  0.139394  0.583030  1.593939  0.363636  2.121212

# There are almost 70% males in the dataframe
# most female are sick
# most male are healthy
# the sick are more like to be:
# younger than the healty (around 52)
# female
# higher chest pain type
# lower resting blood pressure
# lower cholestoral
# lower fasting blood sugar
# higher resting electrocardiographic results
# higher maximum heart rate achieved
# lower exercise induced angina
# lower ST depression induced by exercise relative to rest
# higher slope of the peak exercise ST segment
# lower number of major vessels (0-3) colored by flourosopy
# lower thalium stress result

# categories which might be very important
# sex, cp, ca, exang, oldpeak, slope

# should probably take a look at those values (except for sex which we already kinda looked for)

# sns.countplot(data=df, x="cp", hue="target").set_title("cp")
# plt.show()
# # with a high cp it is quite likely to be sick and with a low cp it is quite likely to be healthy
# sns.countplot(data=df, x="ca", hue="target").set_title("ca")
# plt.show()
# # with a low ca it is quite likely to be sick
# sns.countplot(data=df, x="exang", hue="target").set_title("exang")
# plt.show()
# # with a low exang it quite likely to be sick and with a high it is likely to be healthy
# sns.countplot(data=df, x="oldpeak", hue="target").set_title("oldpeak")
# plt.show()
# # it is extremely likely to be sick with a low oldpeak and extremely likely to be healthy with a high oldpeak
# sns.countplot(data=df, x="slope", hue="target").set_title("slope")
# plt.show()
# # not sure how good the slope category is:
# # equal chances for 0
# # likely healthy for 1
# # likely sick for 2
# # might confuse the algo a bit?


# features = ['age', 'cp', 'ca', 'oldpeak', 'slope', 'exang', 'trestbps', 'sex', 'chol', 'fbs', 'restecg', 'thalach', 'thal']
features = list(df.columns)
features.remove('target')
X = df[features]
Y = df['target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=23)

regressor = LogisticRegression(solver='lbfgs', max_iter=300)

regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)

tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred).ravel()

percision = (tp + tn) / len(Y_pred)
recall = tp / (tp + fn)

print(f"percision: {percision}\nrecall: {recall}\n")
# with a 1000 iterations
# percision: 0.819672131147541
# recall: 0.8709677419354839

# with 400 iterations
# percision: 0.8360655737704918
# recall: 0.8709677419354839

# wtf?

# with 300 iterations
# percision: 0.8524590163934426
# recall: 0.8709677419354839

# naniiiiiiiiiiiiiiiiiiiiiii???????????????????????

f1 = 2 * (percision * recall) / (percision + recall)
print(f"f1 score: {f1}")
# f1 score: 0.8445417578980293


























