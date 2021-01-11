# 从一组日期向量中选择一个或多个日期值
import pandas as pd
# 创建数据帧
dataframe = pd.DataFrame()

dataframe['date'] = pd.date_range('1/1/2021', periods=100000, freq='H')

data = dataframe[(dataframe['date'] > '2021-01-01 01:00:00') &
                 (dataframe['date'] <= '2021-01-01 04:00:00')]

print(data)
#                  date
# 2 2021-01-01 02:00:00
# 3 2021-01-01 03:00:00
# 4 2021-01-01 04:00:00

# 方法2：将日期这一列设为数据帧的索引列，然后用loc进行筛选
dataframe = dataframe.set_index(dataframe['date'])
data2 = dataframe.loc['2021-1-1 01:00:00':'2021-01-01 04:00:00']
print(data2)
# date
# 2021-01-01 01:00:00 2021-01-01 01:00:00
# 2021-01-01 02:00:00 2021-01-01 02:00:00
# 2021-01-01 03:00:00 2021-01-01 03:00:00
# 2021-01-01 04:00:00 2021-01-01 04:00:00