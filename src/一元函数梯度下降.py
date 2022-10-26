# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 22:21
# @Author  : Nickel_Chieh
# @Software: PyCharm

from matplotlib import pyplot as plt
from mpl_toolkits import axisartist
import numpy as np


def object_function(x):
    return x**2 + 3


def grad(w):
    return 2*w


def grad_descent(x_current, learning_rate, precision, iters_max):
    for i in range(iters_max):
        x_before = x_current
        print('第', i, '次迭代x值为:', x_current)
        grad_current = grad(x_current)
        if abs(grad_current) < precision:
            break
        else:
            x_current = x_current - grad_current * learning_rate
            ax.annotate("",
                        xy=(x_current, object_function(x_current)),
                        xytext=(x_before, object_function(x_before)),
                        size=10, va="center", ha="center",
                        arrowprops=dict(color='red',
                                        arrowstyle="simple",
                                        connectionstyle="arc3,rad=0.4",
                                        )
                        )
    print('极小值处为: ', x_current)


fig = plt.figure(figsize=(8, 8))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0, 0)
ax.axis["x"].set_axisline_style("->", size=1.0)
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("-|>", size=1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")
x = np.linspace(-10, 10, 10000)
y = object_function(x)
plt.xlim(-8, 8)
plt.ylim(-5, 35)
plt.plot(x, y)
np.random.seed(5100)
grad_descent(x_current=np.random.randn()*(-10),
             learning_rate=0.1,
             precision=0.000001,
             iters_max=10000)
plt.show()