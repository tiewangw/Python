# 计算一个时间序列数据帧对某个滚动时间的统计量
import pandas as pd

time_index = pd.date_range('1/1/2021',periods=5,freq='M')
# 设置索引
dataframe = pd.DataFrame(index=time_index)

dataframe['Stock_price'] = [1,2,3,4,5]
# 计算滚动平均值
print(dataframe.rolling(window=2).mean())
#             Stock_price
# 2021-01-31          NaN
# 2021-02-28          1.5
# 2021-03-31          2.5
# 2021-04-30          3.5
# 2021-05-31          4.5

