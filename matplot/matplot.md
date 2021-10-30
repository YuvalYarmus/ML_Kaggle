# matplotlib

We will start by making a list of points.
We will do so using numpy.
First we will get familiar with the methods.

```py
x1 = np.linspace(0, 20, num=5, endpoint=True)
x2 = np.linspace(0, 20, num=5, endpoint=False)
y = np.zeros(5)

# difference between x1 and x2
plt.plot(x1, y + 1.5, 'go--', label="endpoint=True ==> /num")
plt.plot(x2, y, 'ko--', label="endpoint=False ==> /num-1")
for i, j in zip(x1, y + 1.5):
   plt.text(i-0.2, j+0.1, '({}, {})'.format(i, j))
for i, j in zip(x2, y):
   plt.text(i-0.2, j+0.1, '({}, {})'.format(i, j))
plt.ylim([-1, 3])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Endpoint difference")
plt.legend()
plt.show()
```
![Endpoint difference](./pngs/Figure_2.png?raw=true "Endpoint difference")

We may want more points in the future, therfore:
```py
NUMS = 100

x1 = np.linspace(-10, 10, num=NUMS, endpoint=True)
x2 = np.linspace(-10, 10, num=NUMS, endpoint=False)
y = np.zeros(NUMS)
```

## starting to plot

```py
y =  x1 ** 2 # creating a parabola
plt.plot(x1 , y, "ko--", label="parabolic")
# ko-- = a black dots with a stripped line between them
# the label will be line's style next to the label's title and will show up on the graph
plt.xlabel("X") # adding a label for x axis
plt.ylabel("Y") # adding a label for the y axis
plt.title("Title") # adding a title above the axes
plt.legend() # plots the labels

plt.show() # shows the entire graph
```
![A Parabola](./pngs/graph2.png?raw=true "Title: Parabola")

## adding a line

```py
plt.plot(x1, (x1 / 10) ** 2, 'go--') # a parabola
plt.plot(x2, y + 0.5, 'ko--') # a straight line where each point has a coordinate of (x, 0.5)
plt.ylim([-0.5, 1]) # setting the range of the y axis
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Title")

plt.show()
```

![2 Lines](./pngs/Figure_1.png?raw=true "Title: 2 Lines")

**for more information on matplotlib plot: </br> https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html**

## subplots
```py
colors = ['r', 'g', 'b', 'k']
fig, axes = plt.subplots(nrows=1, ncols=4)
for axis, color in zip(axes, colors):
    axis.plot(x1, x1 ** 2, color)
plt.tight_layout()
plt.show()
# notice  that if nrows had been 2, axes would have been a numpy.ndarray (2d matrix).
```
![A Subplot](./pngs/Figure_3.png?raw=true "Title: A Subplot")


### 2d subplots
```py
# an example on a 2d matrix
colors = ['r', 'g', 'b', 'k']
colors2 = ['y', 'c', 'm', 'k']
fig, axes = plt.subplots(nrows=2 ,ncols=4)
for row in axes:
    for axis, color, color2 in zip(row, colors, colors2):
        axis.plot(x1**2, x1, color)
        axis.plot(x1, x1**2, color2)
plt.tight_layout()
plt.show()
```
![A 2d Subplot](./pngs/Figure_4.png?raw=true "Title: A 2d Subplot")
```py
# an example on a 2d matrix
# colors = list(mcolors.BASE_COLORS.values())
# colors = list(mcolors.TABLEAU_COLORS.values())
# colors = list(mcolors.CSS4_COLORS.values())
colors = ['b' , 'g' , 'k', 'c' , 'r', 'y' , 'r' , 'k']
colors2 = colors[::-1]
fig, axes = plt.subplots(nrows=2 ,ncols=4, figsize=(9, 3))
# figsize determines the figure ratio
for row in axes:
    for axis, color, color2 in zip(row, colors, colors2): 
        axis.plot(x1**2, x1, color)
        axis.plot(x1, x1**2, color2)
plt.tight_layout()
plt.show()
```
![A 2d Subplot](./pngs/Figure_5.png?raw=true "Title: A 2d Subplot")

__for more information on matplotlib subplots: </br> https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html__

## framing a figure
```py
# figure bounds between 0 and 1
fig = plt.figure()
# fig.add_axes([left_x_position, buttom_y_position, x_len, y_len])
y = x1**2
axis1 = fig.add_axes([0.05, 0.05, 1 - 0.05*2, 1- 0.05*2])
axis2 = fig.add_axes([0.08, 0.08, 0.2, 0.2])
axis1.plot(x1 , y, 'r')
axis2.plot(y , x1, 'g')
plt.show()
```
![framing a figure](./pngs/Figure_6.png?raw=true "Title: framing a figure")



## some styles
```py
# line styles
fig , axis = plt.subplots(figsize=(9, 6))
# marker
axis.plot(x1,x1, marker="+")
axis.plot(x1,x1+1*2, marker="o")
axis.plot(x1,x1+2*2, marker="s")
axis.plot(x1,x1+3*2, marker="*")
# colors
axis.plot(x1,x1+4*2+2, color="red")
axis.plot(x1,x1+5*2+2, color="green")
axis.plot(x1,x1+6*2+2, color="purple")
axis.plot(x1,x1+7*2+2, color="blue")
axis.plot(x1,x1+8*2+2, color="gray")
axis.plot(x1,x1+9*2+2, color="black")
axis.plot(x1,x1+10*2+2, color="yellow")
axis.plot(x1,x1+11*2+2, color="cyan")
# line types
axis.plot(x1,x1+13*2+4, ls=":")
axis.plot(x1,x1+14*2+4, ls="-")
axis.plot(x1,x1+15*2+4, ls="-.")
axis.plot(x1,x1+16*2+4, ls="--")
# mix
axis.plot(x1,x1+17*2+6, ls="-.", marker="+", color="red")
axis.plot(x1,x1+18*2+6, ls=":", marker="*", color="green")
plt.show()
```
![some styles](./pngs/Figure_7.png?raw=true "Title: some styles")


## scatter
```py
# scatter
fig, axis = plt.subplots(figsize=(10, 10))
y = x1 ** 2
axis.scatter(x1, y)
plt.show()
```
![scatter](./pngs/Figure_8.png?raw=true "Title: scatter")


## diagrams
Histograms highlight frequency while boxplots highlight the range of the data.
![diagrams](./pngs/diagrams.png?raw=true "Title: diagrams")
### histogram
```py
import random
rnds = [random.randint(1, 100) for _ in range(100)]
plt.hist(rnds)
plt.show()
```
![histogram](./pngs/Figure_9.png?raw=true "Title: histogram")
### boxplot
```py
import random
rnds = [random.randint(1, 100) for _ in range(100)]
values = [25] * 100
values2 = [i%3 *50 for i in range(100)]
values3 = [20 + i%3 * 2 for i in range(100)] +[90, 70, 50]
fig , axis = plt.subplots()
axis.boxplot([values, values2, values3, rnds],notch=True, meanline=True,
labels=["values", "values2", "values3", "randoms"], vert=True, patch_artist=True, showmeans=True)
# patch_artist adds the blue color to the boxes
# the 0 makes the boxes (1 is a notched box)
# adding the 'rs' option will make the boxes horizontal, another option is to change vert to False
# patch_artist adds the blue color to the boxes
plt.show()
```
*the orange line is the median*
*the black pointer/marker shows the range between the low and high point*
*the green triangle shows the arithmetic means (if meanline=False)*
*the dashed green line shows the mean*
*the boxes as a whole mark reasonable range for the next number in the series to be in*
*The notches represent the confidence interval (CI) around the median (probably where the next number is very likely to be)*
![boxplot](./pngs/Figure_10.png?raw=true "Title: boxplot")
**for more information on matplotlib boxplot: 
</br> https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html
</br> https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot**


## Markers
character 	description </br>
'.' 	point marker </br>
',' 	pixel marker </br>
'o' 	circle marker </br>
'v' 	triangle_down marker </br>
'^' 	triangle_up marker </br>
'<' 	triangle_left marker </br>
'>' 	triangle_right marker </br>
'1' 	tri_down marker </br>
'2' 	tri_up marker </br>
'3' 	tri_left marker </br>
'4' 	tri_right marker </br>
'8' 	octagon marker </br>
's' 	square marker </br>
'p' 	pentagon marker </br>
'P' 	plus (filled) marker </br>
'*' 	star marker </br>
'h' 	hexagon1 marker </br>
'H' 	hexagon2 marker </br>
'+' 	plus marker </br>
'x' 	x marker </br>
'X' 	x (filled) marker </br>
'D' 	diamond marker </br>
'd' 	thin_diamond marker </br>
'|' 	vline marker </br>
'_' 	hline marker </br>

## Line Styles
character 	description </br>
'-' 	solid line style </br>
'--' 	dashed line style </br>
'-.' 	dash-dot line style </br>
':' 	dotted line style </br>

## Colors
The supported color abbreviations are the single letter codes </br>
character 	color </br>
'b' 	blue </br>
'g' 	green </br>
'r' 	red </br>
'c' 	cyan </br>
'm' 	magenta </br>
'y' 	yellow </br>
'k' 	black </br>
'w' 	white </br>