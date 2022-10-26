# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 9:55
# @Author  : Nickel_Chieh
# @Software: PyCharm

# Tools
import numpy as np
import matplotlib.pyplot as plt

# load Data
x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2, 1.3, 2.6, 2.4, 2.3])
y_train = np.array([250, 300, 480, 430, 630, 730, 400, 550, 600, 450])
fig = plt.figure()
plt.scatter(x_train, y_train, c='r', marker='x')
plt.title('Function of x')
plt.xlabel('x')
plt.ylabel('f_wb(x)')
plt.show()


def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        cost += (w * x[i] + b - y[i]) ** 2
    cost /= 2 * m
    return cost


def compute_gradient(x, y, w, b):
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0
    for i in range(m):
        dj_dw += (w * x[i] + b - y[i]) * x[i]
        dj_db += (w * x[i] + b - y[i])
    dj_dw /= m
    dj_db /= m
    return dj_dw, dj_db


def gradient_descent(x, y, w_initial, b_initial, alpha, num_iters, error, cost_function, gradient_function):
    w = w_initial
    b = b_initial
    w_past = 0
    b_past = 0
    w_hist = []
    b_hist = []
    cost_hist = []
    for i in range(num_iters):
        w_hist.append(w)
        b_hist.append(b)
        cost_hist.append(cost_function(x, y, w, b))
        if abs(w-w_past) < error and abs(b-b_past) < error:
            break
        else:
            w_past = w
            b_past = b
            dj_dw, dj_db = gradient_function(x, y, w, b)
            tmp_w = w - alpha * dj_dw
            tmp_b = b - alpha * dj_db
            w = tmp_w
            b = tmp_b
    for i in range(len(w_hist)):
        print(f'Iteration {i:4d}: w {w_hist[i]:8f} b {b_hist[i]:8f} | cost: {cost_hist[i]}')
    return w, b

# Cost function
def plot_costFunction():
    lis_w = np.linspace(0, 500, 100)
    lis_b = np.linspace(-500, 500, 100)
    J_wb = np.zeros(lis_w.shape[0] * lis_b.shape[0])
    J_wb = J_wb.reshape(lis_w.shape[0], lis_b.shape[0])
    for i in range(lis_w.shape[0]):
        for j in range(lis_b.shape[0]):
            J_wb[i][j] = compute_cost(x_train, y_train, lis_w[i], lis_b[j])
    w, b = np.meshgrid(lis_w, lis_b)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.xlabel('w')
    plt.ylabel('b')
    ax.plot_surface(w, b, J_wb, rstride=1, cstride=1, cmap=plt.cm.rainbow)
    plt.show()


if __name__ == '__main__':
    plot_costFunction()
    local_minima_w, local_minima_b = gradient_descent(x_train, y_train, 200, 50, 0.1, 10000, 1e-5,
                                                      compute_cost, compute_gradient)
    print('The local minima of w is', local_minima_w)
    print('The local minima of b is', local_minima_b)
    fig = plt.figure()
    plt.scatter(x_train, y_train, c='r', marker='x')
    plt.plot(x_train, [local_minima_w * x + local_minima_b for x in x_train])
    plt.title("Function of x")
    plt.xlabel("x")
    plt.ylabel("f_wb(x)")
    plt.show()