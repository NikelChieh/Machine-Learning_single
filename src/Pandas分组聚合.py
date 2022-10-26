# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 22:47
# @Author  : Nickel_Chieh
# @Software: PyCharm

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# 创建字典
data = {'A': [1, 2, 2, 3, 2, 4],
        'B': [2014, 2015, 2014, 2014, 2015, 2017],
        'C': ["a", "b", "c", "d", "e", "f"],
        'D': [0.5, 0.9, 2.1, 1.5, 0.5, 0.1]
        }
df = pd.DataFrame(data)
print(df, end='\n\n')

'''
分组
通常我们将数据分成多个集合的操作称之为分组，Pandas中使用groupby()函数来实现分组操作
'''
# df.groupby("B")  # 单列分组(df根据单列进行分组)  返回的是一个groupby对象
# # 对分组后的子集进行数值运算时，不是数值的列会自动过滤
# # 单列分组(df根据单列进行分组)
# for name, data in df.groupby("B"):
#     print(name)
#     print(data)

# # 多列分组
# for name, data in df.groupby(["B", "C"]):
#     print(name)
#     print(data)


# # 选取数据帧中的一列作为index进行分组
# # df的 A 列根据 B 进行分组
# for name, data in df["A"].groupby(df["B"]):
#     print(name)
#     print(data)

# # 数据类型分组
# for name, data in df.groupby(df.dtypes, axis=1):
#     print(name)
#     print(data)

# # # 传入字典分组
# dic = {"A": "number", "B": "number", "C": "str", "D": "number"}
# for name, data in df.groupby(dic, axis=1):
#     print(name)
#     print(data)


# 对分组进行迭代
# GroupBy对象支持迭代，可以产生一组二元元组（由分组名和数据块组成）
# for name, data in df.groupby("A"):
#     print(name)
#     print(data, end='\n\n')


'''
聚合
聚合函数为每个组返回单个聚合值。当创建了groupby对象，就可以对分组数据执行多个聚合操作。比较常用的是通过聚合函数或等效的agg方法聚合

函数名	        说明
count	        分组中非空值的数量
sum	            非空值的和
mean	        非空值的平均值
median	        非空值的中位数
std、var	    无偏标准差和方差
min、max	    非空值的最小和最大值
prod	        非空值的积
first、last	    第一个和最后一个非空值
'''


# # 应用单个聚合函数
# # 对分组后的子集进行数值运算时，不是数值的列会自动过滤
# print(df.groupby("B").mean())
# print(df.groupby("B").sum())

# # 应用多个聚合函数
# print(df.groupby("B").agg([np.sum, np.mean, np.std]))

# def result(x):
#     return x.max() - x.min()
#
#
# print(df.groupby("B").agg(result))  # 求每一组最大值与最小值的差

# 对不同的列使用不同的聚合函数
mapping = {"A": np.sum, "D": np.mean}
print(df.groupby("B").agg(mapping))