# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 9:45
# @Author  : Nickel_Chieh
# @Software: PyCharm

import numpy as np


def gradient_descent(initial_theta, eta=0.05, n_iters=1000, epslion=1e-8):
    """
    梯度下降
    :param initial_theta: 参数初始值，类型为float
    :param eta: 学习率，类型为float
    :param n_iters: 训练轮数，类型为int
    :param epslion: 容忍误差范围，类型为float
    :return: 训练后得到的参数
    """

    theta = initial_theta
    i_iter = 0
    while i_iter < n_iters:
        gradient = 2 * (theta - 3)
        last_theta = theta
        theta = theta - eta * gradient
        if abs(theta - last_theta) < epslion:
            break
        i_iter += 1
    return theta
    # ********** End **********#


if __name__ == '__main__':
    np.random.seed(100)
    theta = np.random.rand()
    print(3.0 - gradient_descent(theta))
