# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 15:48
# @Author  : Nickel_Chieh
# @Software: PyCharm
import pandas as pd

'''
透视表
透视表是各种电子表格程序和其他数据分析软件中一种常见的数据汇总工具
它根据一个或多个键对数据进行聚合，并根据行和列上得分组建将数据分配到各个矩形区域中
在pandas中，可以通过pivot_table函数创建透视表
'''
'''
pivot_table的参数:
pd.DataFrame.pivot_table(self, values=None, index=None, columns=None, ggfunc='mean', fill_value=None, margins=False,
                         dropna=True, margins_name='All')
参数名	        说明
values	        待聚合的列的名称。默认聚合所有数值列
index	        用于分组的列名或其他分组键，出现在结果透视表的行
columns	        用于分组的列名或其他分组键，出现在结果透视表的列
aggfunc	        聚合函数或函数列表，默认为mean，可以是任何对groupby有效的函数
fill_value	    用于替换结果表中的缺失值
dropna	        boolean值，默认为True
margins_name	string，默认为‘ALL’，当参数margins为True时，ALL行和列的名字, 统计总和
'''
data = {'A': [1, 2, 2, 3, 2, 4],
        'B': [2014, 2015, 2014, 2014, 2015, 2017],
        'C': ["a", "b", "c", "d", "e", "f"],
        'D': [0.5, 0.9, 2.1, 1.5, 0.5, 0.1]
        }
df = pd.DataFrame(data)
print(df)
print(df.pivot_table(index="B", columns="C", values="A",
                     aggfunc=sum, margins=True))


'''
交叉表
交叉表是一种用于计算分组频率的特殊透视表。通常使用crosstab函数来创建交叉表
crosstab的参数:
pd.crosstab(index=None,columns=None,values=None,rownames=None
            colnames=None,aggfunc=None,margins=False,dropna=True,normalize=False)
            
其中rownames可以设置行名，colnames可以设置列名，而且前两个参数可以是数组、Series或数组列表
'''
print(pd.crosstab(index=[df["B"], df["A"]], columns=df["C"], values=df["A"], aggfunc=sum, margins=True))



