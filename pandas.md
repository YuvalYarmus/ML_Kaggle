# Pandas DataFrame
sort of like a dictionary with 2 axis - column and index
you can acess an index or a column to get a Series
the default axis (axis=0) are the indexs
</br>

## Creating a DataFrame with numpy:
df = pd.DataFrame(
np.random.randint(1, 10, (3,3)),
index = [1 , 2, 3],
column = [ 'a', 'b', 'c']
)
</br>

## Math operations
number methods such as addition subtraction, multiplication, etc
```py
df['w'] = df['a'] + df['b']
df['w'] = df['a'] - df['b']
df['w'] = df['a'] * df['b']
```
## Access
- access to columns
```py
df[ ['a', 'b'] ]
```
- access to indexes 
  - loc - locks on a specific index by name and returns the matching series
  ```py
  df.loc[ [1 , 2] ]
  ```
  - iloc - locks on a specific index by items index number and returns the matching series
  ```py
  df.iloc[ [1 , 2] ]
  ```

- access to a specific cell
```py
df.loc[ 1, 'a' ]
df.iloc[ 0, 0 ]
```

## Boolean
- to get a true or false
```py
df > 3
df[1] > 3
```
- to get the items in case True and Nan in case False
```py
df[df>3]
```
- to get the Series and adding complex booleans (for columns)
```py
df[(df['a'] > 0) & (df['b'] > 3)]
df.loc[df['a'] > df['b']]
```

## Pandas DataFrame methods
- remove a column or index </br>
__use inplace=True in order to make it a void function (which will change the og reference) instead of a return which will return a new copy__
```py
df.drop(1, inplace=True)
df.drop('a', axis=1)
```

- shape </br>
returns the amount of rows and columns
```py
df.shape
```
- describe </br>
describes all numerical columns (min, max, mean, etc)
```py
df.describe()
```

- uniqe </br>
return the Series without as an array with no duplicates
```py
df['a'].unique()
```

- value counts </br>
counts how many times each value in a series appears
```py
df['a'].value_counts()
```

- sort </br>
sorts the rows by a column
```py
df.sort_values(by='b')
```

- apply </br>
apply a function on a column
```py 
def add_one(x):
    return x + 1
df = df['a'].apply(add_one)
df = df['a'].apply(lambda x: x + 1)
df = df['a'].apply(str) - turns all the values to a string (object)
```

- sum </br>
return the sum of all the values in a column
```py
df['a'].sum()
```
- mean </br>
return the mean of all the values in a column
```py
df['a'].mean()
```
- min </br>
return the min of all the values in a column
```py
df['a'].min()
```
- max </br>
return the max of all the values in a column
```py
df['a'].max()
```

- corr </br>
return the correlation of all the values between the columns
```py
df.corr()
```

- dropna </br>
drops rows in which there are Nan values
```py
df.dropna()
```
to drop the columns
```py
df.dropna(axis=1)
```
__to keep the change add inplace=True__ </br>
__to add a min threshhold of non nan values add thresh=[the threshhold]__

- concat </br>
concatanate DataFrame
```py
df3 = pd.concat([df1, df2])
# to add horizontally
df3 = pd.concat([df1, df2], axis=1)
```
for more info and other similar methods to concat:
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

- reset index </br>
moves the old index list to a new column and creates a new index numbered column
```py
df.reset_index(inplace=True)
# to remove the added column: 
df.drop('index', axis=1, inplace=True)
```

- groupby </br>
group based on a specific category
```py
df.groupby('index')
df.groupby('category')["category1", "category2"].sum()
df.groupby('category').mean()
```

- csv </br>
save the data frame as a csv file and read it
```py
df.to_csv("my_csv.csv", index=False)
data = pd.read_csv("my_csv.csv")
```
- excel </br>
save the data frame as a xlsx file and read it
```py
df.to_excel("my_csv.xlsx", index=True)
data = pd.read_excel("my_csv.xlsx")
```

