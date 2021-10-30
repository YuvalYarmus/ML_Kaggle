import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.metrics import confusion_matrix,  classification_report

df = pd.read_csv('diabetes.csv')
X_features = df.columns.difference(['Outcome'])

print(df.shape, end="\n\n")
print(df.head(), end="\n\n")
print(df.describe(), end="\n\n")
print(df.count(), end="\n\n")
print("\ninfo:")
df.info()
print("\n")

# to make sure there isnt a category with huge values which will thus
# dominate our algorithm, we will try to normalize the values with the StandardScaler
scaler = StandardScaler()
scaler.fit(df.drop('Outcome', axis=1))
scaled = scaler.transform(df.drop('Outcome', axis=1))
scaled = pd.DataFrame(scaled, columns=X_features)
print(scaled.head(), end="\n\n")
print(scaled.describe(), end="\n\n")


X = df[X_features]
Y = df.Outcome


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
X_test, X_validation, Y_test, Y_validation = train_test_split(X_test, Y_test, test_size=0.33 , random_state=42)

classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train, Y_train)

Y_validation_pred = classifier.predict(X_validation)
tn, fp, fn, tp = confusion_matrix(Y_validation, Y_validation_pred).ravel()
percision = (tp + tn) / len(Y_validation_pred)
recall = tp / (tp + fn)
f1 = 2 * (percision * recall) / (percision + recall)
print(f"percision:{percision}\nrecall: {recall}\nf1: {f1}\n")
print(classification_report(Y_validation, Y_validation_pred))


# trying to find a k with a min error percentage between the y_pred and the y_true
min_error_percentage = 1
min_error_k = 1
for k in range(1, 100):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    knn_pred = knn.predict(X_test)
    error_percentage = np.mean(knn_pred != Y_test)
    if(error_percentage < min_error_percentage):
        min_error_percentage = error_percentage
        min_error_k = k

print(f"\nk: {min_error_k}\neror: {min_error_percentage}\n")

knn = KNeighborsClassifier(n_neighbors=min_error_k)
knn.fit(X_train, Y_train)
knn_validation_pred = knn.predict(X_validation)

tn, fp, fn, tp = confusion_matrix(Y_validation, knn_validation_pred).ravel()
percision = (tp + tn) / len(knn_validation_pred)
recall = tp / (tp + fn)
f1 = 2 * (percision * recall) / (percision + recall)
print(f"percision:{percision}\nrecall: {recall}\nf1: {f1}\n")
print(classification_report(Y_validation, knn_validation_pred))


