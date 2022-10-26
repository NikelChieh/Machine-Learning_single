# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 16:17
# @Author  : Nickel_Chieh
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
为什么要进行标准化
对于大多数数据挖掘算法来说，数据集的标准化是基本要求
这是因为，如果特征不服从或者近似服从标准正态分布（即，零均值、单位标准差的正态分布）的话，算法的表现会大打折扣
实际上，我们经常忽略数据的分布形状，而仅仅做零均值、单位标准差的处理
在一个机器学习算法的目标函数里的很多元素所有特征都近似零均值，方差具有相同的阶
如果某个特征的方差的数量级大于其它的特征，那么，这个特征可能在目标函数中占主导地位，这使得模型不能从其它特征有效地学习
"""
from sklearn import preprocessing
import numpy as np

# 创建数组
X_train = np.array([[1., -1., 2.],
                    [2., 0., 0.],
                    [0., 1., -1.]])
print(X_train)

'''
Z-score标准化
这种方法基于原始数据的均值mean和标准差standard deviation进行数据的标准化
将特征A的原始值x使用z-score标准化到x’
z-score标准化方法适用于特征A的最大值和最小值未知的情况，或有超出取值范围的离群数据的情况
将数据按其特征(按列进行)减去其均值，然后除以其方差
最后得到的结果是，对每个特征/每列来说所有数据都聚集在0附近，方差值为1
函数scale为数组形状的数据集的标准化提供了一个快捷实现
'''
X_scaled = preprocessing.scale(X_train)
print(X_scaled)
print(X_scaled.mean(axis=0))  # 零均值
print(X_scaled.std(axis=0))  # 标准方差


'''
Min-max标准化
Min-max标准化方法是对原始数据进行线性变换
设minA和maxA分别为特征A的最小值和最大值，将A的一个原始值x通过min-max标准化映射成在区间[0,1]中的值x'
可以使用MinMaxScaler实现
'''
min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)
print(X_train_minmax)


'''
MaxAbs标准化
MaxAbs的工作原理与Min-max非常相似，但是它只通过除以每个特征的最大值将训练数据特征缩放至 [-1, 1] 范围内
这就意味着，训练数据应该是已经零中心化或者是稀疏数据
可以使用MaxAbsScale实现
'''
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_maxabs = preprocessing.MaxAbsScaler().fit_transform(X_train)
print(X_train_maxabs)


