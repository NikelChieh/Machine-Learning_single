# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 9:46
# @Author  : Nickel_Chieh
# @Software: PyCharm
import numpy as np

# lis = [["工号", "姓名", "出生年月", "联系电话"],
#        [1, "张三", 1988.12, "13323332333"],
#        [2, "李四", 1987.2, "15966666666"]]
# add = [["居住地址", "户籍地址"],
#        ["江苏省南京市禄口机场宿舍202", "江西省南昌市红谷滩新区天月家园A座2201"],
#        ["江苏省南京市禄口机场宿舍203", "湖南省株洲市天元区新天华府11栋303"]]
# # 在整合的时候是将两个表格（二维数组）在水平方向上堆叠在一起组合起来，拼接成一个新的表格（二维数组）
# # 像这种行为称之为hstack（horizontal stack）
# # NumPy提供了实现hstack功能的函数叫hstack
# a = np.array(lis)
# b = np.array(add)
# print(np.hstack((a, b)))
#
# # 在整合的时候是将两个表格（二维数组）在竖直方向上堆叠在一起组合起来，拼接成一个新的表格（二维数组）
# # 像这种行为称之为vstack（vertical stack）。
# # NumPy提供了实现vstack功能的函数叫vstack
# c = np.array([[3, "王五", 1990.1, "13777777777"], [4, "周六", 1996.4, "13069699696"]])
# print(np.vstack((a, c)))
#
# '''
#     将feature1和feature2横向拼接，然后统计拼接后的ndarray中每列的均值
#     :param feature1:待`hstack`的`ndarray`
#     :param feature2:待`hstack`的`ndarray`
#     :print:类型为`ndarray`，其中的值`hstack`后每列的均值
# '''
# feature1 = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 5]]
# feature2 = [[1], [2], [3]]
# f1 = np.array(feature1)
# f2 = np.array(feature2)
# res = np.hstack((f1, f2))
# ave = np.average(res, axis=0)
# print(ave)


# data = np.array([('Alice', 4, 40), ('Bob', 11, 85.5), ('Cathy', 7, 68.0), ('Doug', 9, 60)],
#                 dtype=[("name", "S10"), ("age", "int"), ("score", "float")])

# # 比较运算符	通用函数
# #   ==	    np.equal
# #   !=	    np.not_equal
# #   <	    np.less
# #   <=	    np.less_equal
# #   >	    np.greater
# #   >=	    np.greater_equal
# print(data['age'] < 10)
# print(data['score'] >= 60)
# print(np.greater_equal(data['score'], 60))
# print((data["age"] / 2) == (np.sqrt(data["age"])))
#
# # 布尔数组作掩码
# # 一种更加强大的模式是使用布尔数组作为掩码，通过该掩码选择数据的子数据集
# print(data[data['score'] >= 60])
# print(data['score'][data['score'] >= 60])

# # 布尔逻辑
# # 结合Python的逐位逻辑运算符一起使用
# # 逻辑运算符	通用函数
# #   &	    np.bitwise_and
# #   |	    np.bitwise_or
# #   ^	    np.bitwise_xor
# #   ~	    np.bitwise_not
# print(np.count_nonzero(data['score'] >= 60))  # 统计数组中True的个数
# print(np.sum(data['score'] >= 60))
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.count_nonzero(arr >= 5, axis=1))  # 统计数组中True的个数, 可以按行（axis=1）列（axis=0）求
# print(np.all(data['age'] > 10))  # 年纪都大于10？
# print(data[data['age'] > 10])
#
# a = [[3, 15, 9, 11, 7], [2, 0, 8, 19, 16], [6, 6, 16, 9, 5], [7, 5, 2, 6, 13]]
# a = np.array(a)
# res = a[a > 10]
# print(res)


# # 花式索引
# # 花式索引（Fancy Indexing）是NumPy用来描述使用整型数组
# # （这里的数组，可以是NumPy的数组，也可以是python自带的list）作为索引的术语，其意义是根据索引数组的值作为目标数组的某个轴的下标来取值。
# # 使用一维整型数组作为索引，如果被索引数组(ndarray)是一维数组，那么索引的结果就是对应位置的元素；
# # 如果被索引数组(ndarray)是二维数组，那么就是对应下标的行
# arr = np.array(['zero', 'one', 'two', 'three', 'four'])
# print(arr[[1, 4]])
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# print(arr[[2, 1]])
# print(arr[[1, 2], [0, 1]])  # 打印arr中第2行第1列与第3行第2列的元素


# # 布尔索引
# # 我们可以通过一个布尔数组来索引目标数组，以此找出与布尔数组中值为True的对应的目标数组中的数据，从而达到筛选出想要的数据的功能
# # 我们可以想办法根据我们的需求，构造出布尔数组，然后再通过布尔索引来实现筛选数据的功能
# performance = np.array([3.25, 3.5, 3.75, 3.5, 3.25, 3.75])
# # print(performance[performance > 3.5])
# boolean = performance > 3.5
# print(boolean)
# print(performance[boolean])
#
# input_data = ["d","a","A","p","b","I","C","K"]
# input_data = np.array(input_data)
# result = input_data[(input_data >= "A") & (input_data <= "Z")]
# print(result)


# # 当两个ndarray对象的形状并不相同的时候，
# # 我们可以通过扩展数组的方法来实现相加、相减、相乘等操作，这种机制叫做广播（broadcasting）
# #
# # 广播的原则：如果两个数组的后缘维度（trailing dimension，即从末尾开始算起的维度）的轴长度相符，
# # 或其中的一方的长度为1，则认为它们是广播兼容的。广播会在缺失或长度为1的维度上进行，这句话是理解广播的核心。
# # 广播主要发生在两种情况，一种是两个数组的维数不相等，但是它们的后缘维度的轴长相符，另外一种是有一方的长度为1。
# arr = np.random.randn(4, 3)
# print(arr)
# arr_mean = arr.mean(axis=0)  # 相当于np.average(arr, axis=0)，求平均值
# print(arr_mean)
# print(arr - arr_mean)
#
# arr1 = np.array([[0, 0, 0],
#                  [1, 1, 1],
#                  [2, 2, 2],
#                  [3, 3, 3]])
# arr2 = np.array([1, 2, 3])
# arr_sum = arr1 + arr2
# print(arr_sum)
#
# arr1 = np.array([[0, 0, 0],
#                  [1, 1, 1],
#                  [2, 2, 2],
#                  [3, 3, 3]])  # arr1.shape = (4,3)
# arr2 = np.array([[1], [2], [3], [4]])  # arr2.shape = (4, 1)
# arr_sum = arr1 + arr2
# print(arr_sum)


