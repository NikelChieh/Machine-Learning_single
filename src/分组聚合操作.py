# -*- coding: utf-8 -*-
# @Time    : 2022/7/21 15:08
# @Author  : Nickel_Chieh
# @Software: PyCharm
import pandas as pd
import numpy as np


# 返回最大值与最小值的差
def sub(df):
    return df.max() - df.min()


df = pd.read_csv("E:\\Python_workspace\\Python_Single\\py\\file\\data\\drinks.csv")
mapping = {"wine_servings": sub, "beer_servings": np.sum}
res = df.groupby("continent").agg(mapping)
print(res)


