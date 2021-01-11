# 处理缺失数据中的缺失值
import pandas as pd
import numpy as np
# 创建日期
time_index = pd.date_range('1/1/2021',periods=5,freq='M')
# 创建数据帧，设置索引
dataframe = pd.DataFrame(index=time_index)
# 创建带缺失值的特征
dataframe['Sales'] = [1.0,2.0,np.nan,np.nan,5.0]

# 对缺失数据进行插值
print(dataframe.interpolate())
#             Sales
# 2021-01-31    1.0
# 2021-02-28    2.0
# 2021-03-31    3.0
# 2021-04-30    4.0
# 2021-05-31    5.0

# 向前填充
print(dataframe.ffill())
#             Sales
# 2021-01-31    1.0
# 2021-02-28    2.0
# 2021-03-31    2.0
# 2021-04-30    2.0
# 2021-05-31    5.0

# 向后填充
print(dataframe.bfill())
#             Sales
# 2021-01-31    1.0
# 2021-02-28    2.0
# 2021-03-31    5.0
# 2021-04-30    5.0
# 2021-05-31    5.0





