# 计算两个日期之间的时间差
import pandas as pd

dataframe = pd.DataFrame()

dataframe['Arrived'] = [pd.Timestamp('01-01-2017'),pd.Timestamp('01-04-2017')]
dataframe['Left'] = [pd.Timestamp('01-01-2017'),pd.Timestamp('01-06-2017')]

print(dataframe['Left'] - dataframe['Arrived'])
# 0   0 days
# 1   2 days
# dtype: timedelta64[ns]


# 移除days字符串
data = pd.Series(delta.days for delta in (dataframe['Left'] - dataframe['Arrived']))
print(data)
# 0    0
# 1    2
# dtype: int64





