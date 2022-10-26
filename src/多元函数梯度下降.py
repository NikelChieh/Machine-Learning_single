# -*- coding: utf-8 -*-
# @Time    : 2022/7/25 22:18
# @Author  : Nickel_Chieh
# @Software: PyCharm
import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d


def object_function(x, y):
    return x ** 2 + y ** 2


def grad(p):
    derivx = 2 * p[0]
    derivy = 2 * p[1]
    return np.array([derivx, derivy])


def grad_descent(grad, p_current, learning_rate, precision, iters_max):
    for i in range(iters_max):
        print('第', i, '次迭代p值为:', p_current)
        grad_current = grad(p_current)
        if np.linalg.norm(grad_current, ord=2) < precision:
            break
        else:
            p_current = p_current - grad_current * learning_rate
    print('极小值处p为: ', p_current)
    return p_current


x, y = np.mgrid[-2: 2: 20j, -2: 2: 20j]
z = object_function(x, y)
ax = plt.subplot(111, projection='3d')
ax.set_title('f(x,y)=x^2+y^2')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.cm.Blues_r)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
grad_descent(grad, p_current=np.array([1, -1]), learning_rate=0.1, precision=0.000001, iters_max=10000)
plt.show()