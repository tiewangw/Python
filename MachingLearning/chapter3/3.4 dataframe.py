# 根据某个条件来选择数据帧的行数据

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

# 选择Sex是famale的前2行
result = dataframe[dataframe['Sex'] == 'female'].head(2)
print(result)
#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1


# 多个条件查询
result = dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >=65)]
print(result)