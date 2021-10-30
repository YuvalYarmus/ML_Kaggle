import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
# print(tips.shape)
# print(tips.head())
# print(tips.describe())


# graph = sns.displot(tips.total_bill, bins=100)
# graph2 = sns.displot(tips.tip, bins = 100)
# plt.show()


# sns.pairplot(tips)
# plt.show()


# sns.regplot(data=tips, x='total_bill', y='tip')
# plt.show()


# sns.lmplot(data=tips, x='total_bill', y='tip', col='time', hue='sex')
# sns.lmplot(data=tips, x='total_bill', y='tip', col='sex', hue='time')
# sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker')
# sns.lmplot(data=tips, x='total_bill', y='tip', hue='day')
# plt.show()


# sns.catplot(data=tips, kind='bar', x='day', y='total_bill', hue="smoker").ax.set_title("bar")
# sns.catplot(data=tips, kind='violin', x='day', y='total_bill', hue="sex").ax.set_title("violin")
# sns.catplot(data=tips, kind='box', x='day', y='total_bill', hue="time").ax.set_title("box")
# plt.show()

# sns.countplot(data=tips, x="smoker", hue="time")
# # countplot can not have y values or a col attribute
# plt.show()


# sns.barplot(data=tips, x="smoker", y="total_bill", hue="time")
# plt.show()


# sns.boxplot(data=tips, x="smoker", y="total_bill", hue="time")
# plt.show()


# sns.violinplot(data=tips, x="smoker", y="total_bill", hue="time")
# sns.violinplot(data=tips, x="smoker", y="total_bill", hue="time", split = True)
# plt.show()

total_bill_by_sex_smoker = tips.pivot_table(values="total_bill", index="sex", columns="smoker")
print(total_bill_by_sex_smoker)
# sns.heatmap(total_bill_by_sex_smoker)
sns.heatmap(total_bill_by_sex_smoker, cmap="coolwarm")
plt.show()