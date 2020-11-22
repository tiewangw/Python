 # 替换数据帧中的一些值

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

result = dataframe['Sex'].replace("female","Woman").head(2)
print(result)
# 0    Woman
# 1    Woman
# Name: Sex, dtype: object

# ------------替换多个值-------------
result = dataframe['Sex'].replace(["female","male"],["Woman","Man"]).head(5)
print(result)
# 0    Woman
# 1    Woman
# 2      Man
# 3    Woman
# 4      Man
# Name: Sex, dtype: object


# ---------在整个数据帧中查找和替换值----------

result = dataframe.replace(1,"one").head(2)
print(result)
#                            Name PClass Age     Sex Survived SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29  female      one     one
# 1   Allison, Miss Helen Loraine    1st   2  female        0     one

# -------------用正则表达式替换------------------
result = dataframe.replace(r"1st","First",regex=True).head(5)
print(result)
#                                             Name PClass  ...  Survived SexCode
# 0                   Allen, Miss Elisabeth Walton  First  ...         1       1
# 1                    Allison, Miss Helen Loraine  First  ...         0       1
# 2            Allison, Mr Hudson Joshua Creighton  First  ...         0       0
# 3  Allison, Mrs Hudson JC (Bessie Waldo Daniels)  First  ...         0       1
# 4                  Allison, Master Hudson Trevor  First  ...         1       0









