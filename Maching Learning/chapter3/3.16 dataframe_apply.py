# 遍历数据,对一列的所有元素应用某个函数

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

def uppercase(x):
    return x.upper()

print(dataframe['Name'].apply(uppercase)[0:2])
# 0    ALLEN, MISS ELISABETH WALTON
# 1     ALLISON, MISS HELEN LORAINE
# Name: Name, dtype: object

