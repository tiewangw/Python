# 从数据帧中删除一列

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.head(2))
#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1

# 删除列
print(dataframe.drop('Age', axis=1).head(2))
#                            Name PClass     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  female         1        1
# 1   Allison, Miss Helen Loraine    1st  female         0        1

# 使用一组列名 删除多列
print(dataframe.drop(['Age','Sex'], axis=1).head(2))
#                            Name PClass  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st         1        1
# 1   Allison, Miss Helen Loraine    1st         0        1

# 通过指定列下标删除列
print(dataframe.drop(dataframe.columns[1],axis=1).head(2))
#                            Name   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton  29.0  female         1        1
# 1   Allison, Miss Helen Loraine   2.0  female         0        1


