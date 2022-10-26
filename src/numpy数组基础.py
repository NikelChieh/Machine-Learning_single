import random
import numpy as np
from numpy import *

# a = np.arange(12).reshape(3, 4)
# print(a)
# b = a.reshape((4, 3))
# c = np.reshape(a, (-1, 3))  ## -1即可自动计算所需行数
# print(b)
# print(c)
# a.resize(12)

# lis = [[2, 3, 4, 5], [6, 7, 8, 9]]
# a = np.array(lis)
# a.resize(a.size)
# print(a)


# lis = [[2, 3], [4, 5]]
# a = np.array(lis)
# a = mat(a)
# b = a.I
# print(a*b)
# a = np.array(a)
# b = np.array(b)
# print(a@b)
# print(a.dot(b))
# print(np.dot(a, b))

# info = np.array([[3000, 4000, 20000], [2700, 5500, 25000], [2800, 3000, 15000]])
# # 沿着0号轴统计，结果为[2700, 3000, 15000]
# print(info.min(axis=0))
# # 沿着0号轴统计，结果为[3000, 5500, 25000]
# print(info.max(axis=0))

# lis = [[0.2, 0.7, 0.1], [0.1, 0.3, 0.6]]
# info = np.array(lis)
# print(info.argmax(axis=1))

# random_sample用于生成区间为[0, 1]的随机数，需要填写的参数size表示生成的随机数的形状，比如size=[2, 3]那么则会生成一个2行3列的ndarray，并用随机值填充。
# a = np.random.random_sample(size=[2, 3])
# a = mat(a)
# print(a)

# 如果想模拟像掷骰子、扔硬币等这种随机值是离散值，而且知道范围的可以使用choice实现。choice的主要参数是a、size和replace。
# a是个一维数组，代表你想从a中随机挑选；size是随机数生成后的形状。假如模拟5次掷骰子，replace用来设置是否可以取相同元素，True表示可以取相同数字；False表示不可以取相同数字，默认是True
# b = np.random.choice(range(12), size=[3, 4], replace=False)
# print(b)

# randint的功能和choice差不多，只不过randint只能生成整数，而choice生成的数与a有关，如果a中有浮点数，那么choice会有概率挑选到浮点数。
# randint的参数有3个，分别为low，high和size。其中low表示随机数生成时能够生成的最小值，high表示随机数生成时能够生成的最大值减1。也就是说randint生成的随机数的区间为[low, high)
# c = np.random.randint(1, 7, 10)
# print(c)
# print(6 in c)

# 如果对于产生的随机数的概率分布有特别要求，NumPy同样提供了从指定的概率分布中采样得到的随机值的接口。在这里主要介绍高斯分布
# 高斯分布又称为正态分布
# 其中normal函数除了size参数外，还有两个比较重要的参数就是loc和scale，它们分别代表高斯分布的均值和方差。loc影响的分布中概率最高的点的位置
# scale影响的是分布图形的胖瘦，scale越小，分布就越又高又瘦，scale越大，分布就越又矮又胖
# d = np.random.normal(loc=5, scale=0.5, size=100)
# print(sort(d))

# 前面说了这么多随机数生成的方法，那么随机数是怎样生成的呢？其实计算机产生的随机数是由随机种子根据一定的计算方法计算出来的数值。所以只要计算方法固定，随机种子固定，那么产生的随机数就不会变！
# 如果想要让每次生成的随机数不变，那么就需要设置随机种子（随机种子其实就是一个0到2^32−1的整数）。设置随机种子很长简单，调用seed函数并设置随机种子即可
# np.random.seed(seed=233423)
# data = [1, 2, 3, 4]
# for i in range(10):
#     print(np.random.choice(data))

#打乱列表顺序
# np.random.seed(seed=233)
# lis = [1, 2, 3, 4, 5]
# res = list(np.random.choice(lis, size=len(lis), replace=False))
# print(lis, end=' --> ')
# print(res)



