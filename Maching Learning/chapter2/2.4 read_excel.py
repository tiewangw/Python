# 加载excel数据表

import pandas as pd

# url = 'https://tinyurl.com/simulated_excel'

url = 'F:\\JAVA\\plan.xlsx'
#
dataframe = pd.read_excel(url, sheet_name=0, header=1)
# 查看前2行数据
print(dataframe.head(2))
