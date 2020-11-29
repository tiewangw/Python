# 按照时间段对行分组  ，resample要求索引的类型必须是datetime的值

import pandas as pd
import numpy as np

# 创建日期范围
time_index = pd.date_range('01/11/2020',periods=100000,freq='30S')

# 创建数据帧
dataframe = pd.DataFrame(index=time_index)

# 创建一列随机数
dataframe['Sale_Amount'] = np.random.randint(1,10,100000)

print(dataframe.head(5))
#                      Sale_Amount
# 2020-01-11 00:00:00            9
# 2020-01-11 00:00:30            7
# 2020-01-11 00:01:00            8
# 2020-01-11 00:01:30            2
# 2020-01-11 00:02:00            8

# --------按周对行分组，计算每一周的总和
print(dataframe.resample('W').sum())
#             Sale_Amount
# 2020-01-12        28947
# 2020-01-19       100354
# 2020-01-26       101475
# 2020-02-02       100692
# 2020-02-09       100944
# 2020-02-16        67674


# --------按2周分组，计算平均值
print(dataframe.resample('2W').mean())
#             Sale_Amount
# 2020-01-12     5.002083
# 2020-01-26     5.004762
# 2020-02-09     4.974975
# 2020-02-23     4.988529

# ------按月计算行数
print(dataframe.resample('M').count())
#             Sale_Amount
# 2020-01-31        60480
# 2020-02-29        39520

