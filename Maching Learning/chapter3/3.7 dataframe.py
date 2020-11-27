# 计算一个数值列的最大值、最小值、总和、平均值与计数值

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print('Maximum:',dataframe['Age'].max())
print('Minimum:',dataframe['Age'].min())
print('Mean:',dataframe['Age'].mean())
print('Sum:',dataframe['Age'].sum())
print('Count:',dataframe['Age'].count())

# Maximum: 71.0
# Minimum: 0.17
# Mean: 30.397989417989415
# Sum: 22980.88
# Count: 756

# --------整个数据帧的统计信息-----------
print(dataframe.count())
