# 根据一些共有的值对行进行分组

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

# -----错误方法
print(dataframe.groupby('Sex').mean)
# <bound method GroupBy.mean of <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000020B8DE47108>>


print(dataframe.groupby('Sex').mean())
#               Age  Survived  SexCode
# Sex
# female  29.396424  0.666667      1.0
# male    31.014338  0.166863      0.0


print(dataframe.groupby('Survived')['Name'].count())
# Survived
# 0    863
# 1    450
# Name: Name, dtype: int64


print(dataframe.groupby(['Sex','Survived'])['Age'].mean())
# Sex     Survived
# female  0           24.901408
#         1           30.867143
# male    0           32.320780
#         1           25.951875
# Name: Age, dtype: float64



