# 为一组时间序列数据添加或改变时区

import pandas as pd

date = pd.Timestamp('2020-03-01 10:20:23')
# 设置时区
date_in_london = date.tz_localize('Europe/London')
print(date_in_london)
# 2020-03-01 18:20:23+00:00

# tz_convert 修改时区
print(date_in_london.tz_convert('Africa/Abidjan'))