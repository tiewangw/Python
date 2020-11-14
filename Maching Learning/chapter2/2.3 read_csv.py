# 加载CSV文件（以逗号Comma-Separated Values为分隔符的文件）

import pandas as pd

url = 'https://tinyurl.com/simulated_data'

# pandas库的read_csv加载一个本地或远端的CSV文件
dataframe = pd.read_csv(url)
# 查看前2行数据
print(dataframe.head(2))