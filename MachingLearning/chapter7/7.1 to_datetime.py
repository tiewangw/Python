# 把一个代表日期和时间的字符串向量转换成时间序列数据
import numpy as np
import pandas as pd

date_strings = np.array([
    '03-04-2020 11:35 PM',
    '01-07-2021 12:34 AM',
    '04-09-1990 09:09 PM'
])

# errors="coerce" :当转换出现错误时不会抛出异常，会将值设置成NaT
res = [pd.to_datetime(date,format='%d-%m-%Y %I:%M %p',errors="coerce") for date in date_strings]
print(res)
# [Timestamp('2020-04-03 23:35:00'), Timestamp('2021-07-01 00:34:00'), Timestamp('1990-09-04 21:09:00')]