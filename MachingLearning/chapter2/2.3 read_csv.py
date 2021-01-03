# 加载CSV文件（以逗号Comma-Separated Values为分隔符的文件）

import pandas as pd

# url = 'https://tinyurl.com/simulated_data'
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
# url = 'https://mfr.osf.io/render?url=https://osf.io/aupb4/?direct%26mode=render%26action=download%26mode=render'

# pandas库的read_csv加载一个本地或远端的CSV文件
dataframe = pd.read_csv(url)
# 查看前2行数据
print(dataframe.head(2))

#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1