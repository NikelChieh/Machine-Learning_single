# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 13:01
# @Author  : Nickel_Chieh
# @Software: PyCharm

import numpy as np
from numpy import linalg

# 常用的numpy.linalg函数：
# 函数	    说明
# dot	    矩阵乘法
# vdot	    两个向量的点积
# det	    计算矩阵的行列式
# inv	    计算方阵的逆
# svd	    计算奇异值分解（SVD）
# solve	    解线性方程组 Ax=b，A是一个方阵
# matmul	两个数组的矩阵积

# dot()：该函数返回俩个数组的点积。对于二维向量，效果等于矩阵乘法；
# 对于一维数组，它是向量的内积；对于N维数组，它是a的最后一个轴上的和与b的倒数第二个轴的乘积


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))

# det()：该函数用于计算输入矩阵的行列式
arr = np.array([[1, 2], [3, 4]])
print(linalg.det(arr))

# inv()：该函数用于计算方阵的逆矩阵
# 逆矩阵的定义维如果两个方阵A、B，使得AB = BA = E，则A称为可逆矩阵，B为A的逆矩阵，E为单位矩阵
arr = np.array([[1, 2], [3, 4]])
arr_I = linalg.inv(arr)
print(arr_I)
print(np.dot(arr, arr_I))  # 单位矩阵会有小误差

# solve()：该函数用于计算线性方程的解
# 假设有如下方程组：3x+2y=7  x+4y=14；
# 写成矩阵的形式：[[3,2][1,4]]*[[x],[y]]=[[7],[14]]
a = np.array([[3, 2], [1, 4]])
b = np.array([[7], [14]])
res = linalg.solve(a, b)
print(res)

# matmul()：函数返回两个数组的矩阵乘积
# 如果参数中有一维数组，则通过在其维度上附加1来提升为矩阵，并在乘法之后去除
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.matmul(a, b))
c = np.array([7, 8])
print(np.matmul(a, c))

# svd()：奇异值分解是一种矩阵分解的方法，该函数用来求解SVD
a = [[0, 1], [1, 1], [1, 0]]
print(linalg.svd(a))


