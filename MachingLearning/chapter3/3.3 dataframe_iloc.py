# 从数据帧中挑出单个数据或一部分数据

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

# 选择第一行
print(dataframe.iloc[0])
# Name        Allen, Miss Elisabeth Walton
# PClass                               1st
# Age                                   29
# Sex                               female
# Survived                               1
# SexCode                                1
# Name: 0, dtype: object

# 选择2-4行
print(dataframe.iloc[1:4])

# 选择到第5行为止的所有行
print(dataframe.iloc[:5])

# ------------------------------------
#  数据帧的索引不必非得是数据型，只要某一列在数据帧中每一行的值是唯一的，就可以将其设置为索引。
# 设置索引
dataframe.set_index(dataframe['Name'])
print(dataframe.loc['Allen'])