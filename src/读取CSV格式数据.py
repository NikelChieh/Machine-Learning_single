# -*- coding: utf-8 -*-
# @Time    : 2022/7/17 10:28
# @Author  : Nickel_Chieh
# @Software: PyCharm
import pandas as pd

df = pd.read_csv("E:\\Python_workspace\\Python_Multiple\\Machine-Learning_single\\data\\uk_rain_2014.csv", header=0)
print(df.head(5))
print(df.tail(5))
print(len(df))
df.columns = ['water_year', 'rain_octsep', 'outflow_octsep', 'rain_decfeb', 'outflow_decfeb', 'rain_junaug',
              'outflow_junaug']
print(df.head(5))
