# 计算唯一值

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

# 筛选出唯一值
print(dataframe['Sex'].unique())  # ['female' 'male']

# 唯一值及其出现的次数
print(dataframe['Sex'].value_counts())
# male      851
# female    462


# 查看唯一值的个数
print(dataframe['Age'].nunique())   # 75
print(dataframe['PClass'].nunique())  # 4


