import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


# x1 = np.linspace(0, 20, num=5, endpoint=True)
# x2 = np.linspace(0, 20, num=5, endpoint=False)
# y = np.zeros(5)

# # difference between x1 and x2
# plt.plot(x1, y + 1.5, 'go--', label="endpoint=True ==> /num-1")
# plt.plot(x2, y, 'ko--', label="endpoint=False ==> /num")
# for i, j in zip(x1, y + 1.5):
#    plt.text(i-0.2, j+0.1, '({}, {})'.format(i, j))
# for i, j in zip(x2, y):
#    plt.text(i-0.2, j+0.1, '({}, {})'.format(i, j))
# plt.ylim([-1, 3])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Endpoint difference")
# plt.legend()
# plt.show()


NUMS = 100

x1 = np.linspace(-10, 10, num=NUMS, endpoint=True)
x2 = np.linspace(-10, 10, num=NUMS, endpoint=False)
y = np.zeros(NUMS)
# plt.plot(x1 , x1**2, "ko--", label="parabolic")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Title")
# plt.legend() #plots the label

# plt.show()


# plt.plot(x1, (x1 / 10) ** 2, 'go--')
# plt.plot(x2, y + 0.5, 'ko--')
# plt.ylim([-0.5, 1])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Title")

# plt.show()

# colors = ['r', 'g', 'b', 'k']
# fig, axes = plt.subplots(nrows=1, ncols=4)
# for axis, color in zip(axes, colors):
#     axis.plot(x1, x1 ** 2, color)
# plt.tight_layout()
# plt.show()
# notice  that if nrows had been 2, axes would have been a numpy.ndarray (2d matrix).


# an example on a 2d matrix
# colors = list(mcolors.BASE_COLORS.values())
# colors = list(mcolors.TABLEAU_COLORS.values())
# colors = list(mcolors.CSS4_COLORS.values())
colors = ['b' , 'g' , 'k', 'c' , 'r', 'y' , 'r' , 'k']
colors2 = colors[::-1]

# fig, axes = plt.subplots(nrows=2 ,ncols=4, figsize=(9, 3))
# for row in axes:
#     for axis, color, color2 in zip(row, colors, colors2):
#         axis.plot(x1**2, x1, color)
#         axis.plot(x1, x1**2, color2)
# plt.tight_layout()
# plt.show()


# # figure
# fig = plt.figure()
# # fig.add_axes([left_x_position, buttom_y_position, x_len, y_len])
# y = x1**2
# axis1 = fig.add_axes([0.05, 0.05, 1 - 0.05*2, 1- 0.05*2])
# axis2 = fig.add_axes([0.08, 0.08, 0.2, 0.2])
# axis1.plot(x1 , y, 'r')
# axis2.plot(y , x1, 'g')
# plt.show()


# # scatter
# fig, axis = plt.subplots(figsize=(10, 10))
# y = x1 ** 2
# axis.scatter(x1, y)
# plt.show()


# # line styles
# fig , axis = plt.subplots(figsize=(9, 6))
# # marker
# axis.plot(x1,x1, marker="+")
# axis.plot(x1,x1+1*2, marker="o")
# axis.plot(x1,x1+2*2, marker="s")
# axis.plot(x1,x1+3*2, marker="*")
# # colors
# axis.plot(x1,x1+4*2+2, color="red")
# axis.plot(x1,x1+5*2+2, color="green")
# axis.plot(x1,x1+6*2+2, color="purple")
# axis.plot(x1,x1+7*2+2, color="blue")
# axis.plot(x1,x1+8*2+2, color="gray")
# axis.plot(x1,x1+9*2+2, color="black")
# axis.plot(x1,x1+10*2+2, color="yellow")
# axis.plot(x1,x1+11*2+2, color="cyan")
# # line types
# axis.plot(x1,x1+13*2+4, ls=":")
# axis.plot(x1,x1+14*2+4, ls="-")
# axis.plot(x1,x1+15*2+4, ls="-.")
# axis.plot(x1,x1+16*2+4, ls="--")
# # mix
# axis.plot(x1,x1+17*2+6, ls="-.", marker="+", color="red")
# axis.plot(x1,x1+18*2+6, ls=":", marker="*", color="green")
# plt.show()


# diagrams
import random
rnds = [random.randint(1, 100) for _ in range(100)]

# plt.hist(rnds)
# plt.show()

values = [25] * 100
values2 = [i%3 *50 for i in range(100)]
values3 = [20 + i%3 * 2 for i in range(100)] +[90, 70, 50]
fig , axis = plt.subplots()
axis.boxplot([values, values2, values3, rnds],notch=True, meanline=True,
labels=["values", "values2", "values3", "randoms"], vert=True, patch_artist=True, showmeans=True)
# patch_artist adds the blue color to the boxes
# the notch makes the notched boxes, can also be just 0/1 where 1 is a notched box and 0 rectangular
# adding the 'rs' option will make the boxes horizontal
plt.show()