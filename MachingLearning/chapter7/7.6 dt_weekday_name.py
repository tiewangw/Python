# 求一个日期向量中的每一个日期是星期几
import pandas as pd

dates = pd.Series(pd.date_range('2/2/2021',periods=5,freq='M'))
print(dates)
# 0   2021-02-28
# 1   2021-03-31
# 2   2021-04-30
# 3   2021-05-31
# 4   2021-06-30

# 查看星期几
print(dates.dt.weekday_name)
# 0       Sunday
# 1    Wednesday
# 2       Friday
# 3       Monday
# 4    Wednesday

# 输出数值（星期一是0）
print(dates.dt.weekday)
# 0    6
# 1    2
# 2    4
# 3    0
# 4    2



