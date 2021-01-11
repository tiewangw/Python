# 用一个日期和时间数据来创建年、月、日、时、分的特征

import pandas as pd

dataframe = pd.DataFrame()

dataframe['date'] = pd.date_range('1/1/2021',periods=150,freq='W')

print(dataframe)
#           date
# 0   2021-01-03
# 1   2021-01-10
# 2   2021-01-17
# 3   2021-01-24
# 4   2021-01-31
# ..         ...
# 145 2023-10-15
# 146 2023-10-22
# 147 2023-10-29
# 148 2023-11-05
# 149 2023-11-12

# 创建年、月、日、时、分的特征
dataframe['year'] = dataframe['date'].dt.year
dataframe['month'] = dataframe['date'].dt.month
dataframe['day'] = dataframe['date'].dt.day
dataframe['hour'] = dataframe['date'].dt.hour
dataframe['minute'] = dataframe['date'].dt.minute
# 查看3行
print(dataframe.head(3))
#         date  year  month  day  hour  minute
# 0 2021-01-03  2021      1    3     0       0
# 1 2021-01-10  2021      1   10     0       0
# 2 2021-01-17  2021      1   17     0       0



