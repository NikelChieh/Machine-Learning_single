# -*- coding: utf-8 -*-
# @Time    : 2022/7/17 10:01
# @Author  : Nickel_Chieh
# @Software: PyCharm

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

'''
Pandas中的数据结构

Series: 一维数组，类似于Python中的基本数据结构list，区别是Series只允许存储相同的数据类型，
        这样可以更有效的使用内存，提高运算效率。就像数据库中的列数据；
DataFrame: 二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器；
Panel：三维的数组，可以理解为DataFrame的容器。


了解Series

为了开始使用Pandas，我们必需熟悉它的两个重要的数据结构：Series 和DataFrame。
虽然它们不是每一个问题的通用解决方案，但可以提供一个坚实的，易于使用的大多数应用程序的基础。
Series是一个一维的类似的数组对象，包含一个数组的数据（任何NumPy的数据类型）和一个与数组关联的数据标签，被叫做索引 。
'''
# obj = Series([2, 3, 4, 5])
# print(obj)
# print(obj.values)
# print(obj.index)
#
# obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
# print(obj2)
# print(obj2.values)
# print(obj2.index)
#
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj3 = Series(sdata)
# print(obj3)
# print(obj3.values)
# print(obj3.index)
#
# # DataFrame创建
# dictionary = {'state': ['0hio', '0hio', '0hio', 'Nevada', 'Nevada'],
#               'year': [2000, 2001, 2002, 2001, 2002],
#               'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(dictionary)
# print(frame)
#
# # 修改行名
# frame = DataFrame(dictionary, index=['one', 'two', 'three', 'four', 'five'])
# print(frame)
#
# # 添加修改
# frame['add'] = [0, 0, 0, 0, 0]
# print(frame)
#
# # 添加Series类型
# value = Series([1, 2, 3, 4, 5], index=['one', 'two', 'three', 'four', 'five'])  # Series的长度和索引必须与DataFrame对应，不然会NaN
# frame['add1'] = value
# print(frame)
#
# dictionary = {'states': ['0hio', '0hio', '0hio', 'Nevada', 'Nevada'],
#               'years': [2000, 2001, 2002, 2001, 2002],
#               'pops': [1.5, 1.7, 3.6, 2.4, 2.9]}
# df1 = DataFrame(dictionary, index=['one', 'two', 'three', 'four', 'five'])
# df1['new_add'] = ([7, 4, 5, 8, 2])
# print(df1)
#
# # Series用sort_index()按索引排序，sort_values()按值排序
# obj = Series([2, 1, 4, 3], index=['d', 'b', 'a', 'c'])
# print(obj.sort_index())
# print(obj.sort_values())
#
# # DataFrame也是用sort_index()和sort_values()
# frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
# print(frame)
# print(frame.sort_index())
# print(frame.sort_index(axis=1))
# print(frame.sort_index(axis=1, ascending=False))
# print(frame.sort_index(axis=0))
#
# print(frame.sort_values(by='a', ascending=False))  # 同一列按值排序


# # 删除Series的一个元素
# ser = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# print(ser)
# print(ser.drop('c'))
#
# # 删除DataFrame的行或列
# df = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'c', 'd'], columns=['oh', 'te', 'ca'])
# print(df)
# print(df.drop('c'))
# print(df.drop('oh', axis=1))


'''
Dataframe的加减乘除运算
'''
# df1 = DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
# df2 = DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
# print(df1)
# print(df2)
# print(df1 + df2)
# print((df1 + df2).fillna(0.0))  # 在加法运算结束之后，将NaN转化为0.0
# print(df1.add(df2, fill_value=0.0))  # 在加法运算之前，用0.0补齐空位，使加完之后不出现NaN


'''
去除Dataframe中的重复项
'''
# df = DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [1, 1, 2, 3, 3, 4, 4]})
# print(df, end='\n\n')
# print(df.duplicated(), end='\n\n')  # 找出重复项，返回一个布尔类型的Series
# print(df.drop_duplicates(), end='\n\n')  # 去掉重复项


np.random.seed(seed=100)
data = Series(np.random.randn(10),
              index=[['a'] * 3 + ['b'] * 3 + ['c'] * 2 + ['d'] * 2, [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data['b':'d'])  # 索引'b'到'd'
print(data['a', :])  # 索引'a'的所有数据
print(data[:, 2])  # 索引所有数据的2

# 对Series进行数据重塑，转化成DataFrame类型
frame = data.unstack()
print(frame)
