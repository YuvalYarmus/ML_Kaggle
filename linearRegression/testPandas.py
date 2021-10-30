import pandas as pd
import numpy as np

df = pd.DataFrame(
np.random.randint(1, 10, (3,3)),
index = [1 , 2, 3],
columns = [ 'a', 'b', 'c']
)

print("math")
print(df, end="\n\n")
df['w'] = df['a'] + df['b']
print(df, end = "\n\n")
df['w'] = df['a'] - df['b']
print(df, end = "\n\n")
df['w'] = df['a'] * df['b']
print(df, end = "\n\n")

print("checks")
print(df > 3, end="\n\n")
print(df['a'] > 3, end="\n\n")
print(df.loc[1] > 3, end="\n\n")
print(df[df > 3], end="\n\n")
print(df.loc[df['a'] > df['b']], end="\n\n")


print("drops")
print(df.loc[ [1 , 2] ], end="\n\n")
print(df.iloc[ [1 , 2] ], end="\n\n")
print(df[ ['a', 'b'] ], end = "\n\n")
print(df, end = "\n\n")
print(df.loc[ 1, 'a' ], end = "\n\n")
print(df.iloc[ 0, 0 ], end = "\n\n")
print(df.drop(1), end = "\n\n")
print(df.drop('a', axis=1), end = "\n\n")