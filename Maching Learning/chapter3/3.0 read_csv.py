# 加载CSV文件
import pandas as pd

url = 'https://mfr.osf.io/render?url=https://osf.io/aupb4/?direct%26mode=render%26action=download%26mode=render'

# pandas库的read_csv加载一个本地或远端的CSV文件
dataframe = pd.read_csv(url)
# 查看前2行数据
print(dataframe.head(2))