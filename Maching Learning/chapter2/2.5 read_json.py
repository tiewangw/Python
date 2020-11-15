# 加载json文件

import pandas as pd

# url = 'https://tinyurl.com/simulated_json'
url = '{"city":{"guangzhou":"20","zhuhai":"20"},"home":{"price":"5W","data":"10"}}'
#
dataframe = pd.read_json(url,orient='columns')
# 查看前2行数据
print(dataframe.head(3))