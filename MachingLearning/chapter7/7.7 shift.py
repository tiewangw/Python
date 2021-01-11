# 创建一个滞后n个时间段的特征
import pandas as pd

dataframe = pd.DataFrame()
# 创建数据
dataframe['dates'] = pd.date_range('1/1/2021',periods=5,freq='D')
dataframe['stock_price'] = [1.1,2.2,3.3,4.4,5.5]
# 让值滞后一行
dataframe['previous_days_stock_price'] = dataframe['stock_price'].shift(1)

print(dataframe)
#        dates  stock_price  previous_days_stock_price
# 0 2021-01-01          1.1                        NaN
# 1 2021-01-02          2.2                        1.1
# 2 2021-01-03          3.3                        2.2
# 3 2021-01-04          4.4                        3.3
# 4 2021-01-05          5.5                        4.4
