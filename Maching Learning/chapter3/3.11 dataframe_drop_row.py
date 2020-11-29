# 从数据帧中删除一行

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.head(2))
#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1


# 删除一些行，查看输出结果的前2行
print(dataframe[dataframe['Sex'] != 'male'].head(2))
#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1

# 通过布尔条件删除一行
print(dataframe[dataframe['Name'] != 'Allison, Miss Helen Loraine'].head(2))
#                                   Name PClass   Age     Sex  Survived  SexCode
# 0         Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 2  Allison, Mr Hudson Joshua Creighton    1st  30.0    male         0        0

# 根据下标来删除一行
print(dataframe[dataframe.index != 0].head(2))
#                                   Name PClass   Age     Sex  Survived  SexCode
# 1          Allison, Miss Helen Loraine    1st   2.0  female         0        1
# 2  Allison, Mr Hudson Joshua Creighton    1st  30.0    male         0        0
