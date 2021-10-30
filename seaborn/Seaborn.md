# seaborn
First of all, [a good reading material](https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial)

Seaborn come with prepacked data sets, so we will load one to try and work on it.
```py
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.shape)
print(tips.head())
print(tips.describe())
```

## displot
*do notice not to use dis**t**plot which is deprecated* </br>

Figure-level interface for drawing distribution plots onto a FacetGrid.
This function provides access to several approaches for visualizing the univariate or bivariate distribution of data, including subsets of data defined by semantic mapping and faceting across multiple subplots. The kind parameter selects the approach to use:
- histplot() (with kind="hist"; the default)
- kdeplot() (with kind="kde")
- ecdfplot() (with kind="ecdf"; univariate-only)

```py
graph = sns.displot(tips.total_bill, bins=100)
graph2 = sns.displot(tips.tip, bins = 100)
plt.show()
```
![displot total_bill](./pngs/Figure_1.png?raw=true "displot total_bill")
![displot tip](./pngs/Figure_2.png?raw=true "displot tip")

**for more information on the displot method: </br> https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot**


## pairplot
Plot pairwise relationships in a dataset.

By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.

It is also possible to show a subset of variables or plot different variables on the rows and columns.

This is a high-level interface for PairGrid that is intended to make it easy to draw a few common styles. You should use PairGrid directly if you need more flexibility.
```py
sns.pairplot(tips)
plt.show()
```
![pairplot tip](./pngs/Figure_3.png?raw=true "pairplot tip")
**for more information on the pairplot method: </br> https://seaborn.pydata.org/generated/seaborn.pairplot.html**

## regplot
Plot data and a linear regression model fit.

There are a number of mutually exclusive options for estimating the regression model. See the 
[tutorial](https://seaborn.pydata.org/tutorial/regression.html#regression-tutorial) for more information.
```py
sns.regplot(data=tips, x='total_bill', y='tip')
plt.show()
```
![regplot tip](./pngs/Figure_4.png?raw=true "regplot tip")
**for more information on the regplot method: </br> https://seaborn.pydata.org/generated/seaborn.regplot.html**


## lmplot
Plot data and regression model fits across a FacetGrid.

This function combines regplot() and FacetGrid. It is intended as a convenient interface to fit regression models across conditional subsets of a dataset.

When thinking about how to assign variables to different facets, a general rule is that it makes sense to use hue for the most important comparison, followed by col and row. However, always think about your particular dataset and the goals of the visualization you are creating.

There are a number of mutually exclusive options for estimating the regression model. See the tutorial for more information.

The parameters to this function span most of the options in FacetGrid, although there may be occasional cases where you will want to use that class and regplot() directly.
```py
sns.lmplot(data=tips, x='total_bill', y='tip', col='time', hue='sex')
sns.lmplot(data=tips, x='total_bill', y='tip', col='sex', hue='time')
sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker')
sns.lmplot(data=tips, x='total_bill', y='tip', hue='day')
plt.show()
```
![lmplot time-sex total_bill](./pngs/Figure_5.png?raw=true "lmplot time-sex total_bill")
![lmplot sex-time total_bill](./pngs/Figure_6.png?raw=true "lmplot sex-time total_bill")
![lmplot smoker total_bill](./pngs/Figure_7.png?raw=true "lmplot smoker total_bill")
![lmplot day total_bill](./pngs/Figure_8.png?raw=true "lmplot day total_bill")

**for more information on the lmplot method: </br> https://seaborn.pydata.org/generated/seaborn.lmplot.html**

## catplot
This function provides access to several axes-level functions that show the relationship between a numerical and one or more categorical variables using one of several visual representations. The kind parameter selects the underlying axes-level function to use.
See the [tutorial](https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial) for more information.
```py
sns.catplot(data=tips, kind='bar', x='day', y='total_bill', hue="smoker").ax.set_title("bar")
sns.catplot(data=tips, kind='violin', x='day', y='total_bill', hue="sex").ax.set_title("violin")
sns.catplot(data=tips, kind='box', x='day', y='total_bill', hue="time").ax.set_title("box")
plt.show()
```
![catplot smoker-day total_bill](./pngs/Figure_9.png?raw=true "catplot smoker-day total_bill")
![catplot sex-day total_bill](./pngs/Figure_10.png?raw=true "catplot sex-day total_bill")
![catplot time-day total_bill](./pngs/Figure_11.png?raw=true "catplot time-day total_bill")

**for more information on the catplot method: </br> https://seaborn.pydata.org/generated/seaborn.catplot.html**

## countplot
Show the counts of observations in each categorical bin using bars.
```py
sns.countplot(data=tips, x="smoker", hue="time")
# countplot can not have y values or a col attribute
plt.show()
```
![countplot smoker-time](./pngs/Figure_12.png?raw=true "barplot smoker-time")

**for more information on the countplot method: </br> https://seaborn.pydata.org/generated/seaborn.countplot.html**



## barplot
Show point estimates and confidence intervals as rectangular bars.

A bar plot represents an estimate of central tendency for a numeric variable with the height of each rectangle and provides some indication of the uncertainty around that estimate using error bars. Bar plots include 0 in the quantitative axis range, and they are a good choice when 0 is a meaningful value for the quantitative variable, and you want to make comparisons against it.

For datasets where 0 is not a meaningful value, a point plot will allow you to focus on differences between levels of one or more categorical variables.

It is also important to keep in mind that a bar plot shows only the mean (or other estimator) value, but in many cases it may be more informative to show the distribution of values at each level of the categorical variables. In that case, other approaches such as a box or violin plot may be more appropriate.

```py
sns.barplot(data=tips, x="smoker", y="total_bill", hue="time")
plt.show()
```

![barplot smoker-time total_bill](./pngs/Figure_13.png?raw=true "barplot smoker-time total_bill")

**for more information on the barplot method: </br> https://seaborn.pydata.org/generated/seaborn.barplot.html**


## boxplot
Draw a box plot to show distributions with respect to categories.

A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the inter-quartile range.

```py
sns.boxplot(data=tips, x="smoker", y="total_bill", hue="time")
plt.show()
```

![boxplot smoker-time total_bill](./pngs/Figure_14.png?raw=true "boxplot smoker-time total_bill")

**for more information on the barplot method: </br> https://seaborn.pydata.org/generated/seaborn.boxplot.html**

## violinplot
Draw a combination of boxplot and kernel density estimate.

A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.

This can be an effective and attractive way to show multiple distributions of data at once, but keep in mind that the estimation procedure is influenced by the sample size, and violins for relatively small samples might look misleadingly smooth.

```py
sns.violinplot(data=tips, x="smoker", y="total_bill", hue="time")
sns.violinplot(data=tips, x="smoker", y="total_bill", hue="time", split = True)
plt.show()
```

![violinplot smoker-time total_bill](./pngs/Figure_15.png?raw=true "violinplot smoker-time total_bill")
![violinplot smoker-time total_bill split](./pngs/Figure_16.png?raw=true "violinplot smoker-time total_bill split")

**for more information on the barplot method: </br> https://seaborn.pydata.org/generated/seaborn.violinplot.html**

## heatmap - pivot table
Plot rectangular data as a color-encoded matrix.
```py
total_bill_by_sex_smoker = tips.pivot_table(values="total_bill", index="sex", columns="smoker")
print(total_bill_by_sex_smoker)
# smoker        Yes         No
# sex                         
# Male    22.284500  19.791237
# Female  17.977879  18.105185
# sns.heatmap(total_bill_by_sex_smoker)
sns.heatmap(total_bill_by_sex_smoker, cmap="coolwarm")
plt.show()
```
![heatmap smoker-sex total_bill](./pngs/Figure_17.png?raw=true "violinplot smoker-sex total_bill")
![heatmap smoker-sex total_bill](./pngs/Figure_18.png?raw=true "violinplot smoker-sex total_bill")

**for more information on the heatmap method: </br> https://seaborn.pydata.org/generated/seaborn.heatmap.html**

[GO BACK UP](#seaborn)