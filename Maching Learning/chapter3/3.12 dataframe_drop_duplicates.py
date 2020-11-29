# 从数据帧中删除重复行

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.head(2))
#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1

# --------duplicates 默认只会删除所有列都完美匹配的行
print(dataframe.drop_duplicates().head(2))
#                            Name PClass   Age     Sex  Survived  SexCode
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1

# --------使用参数sunset将Sex重复的删除
print(dataframe.drop_duplicates(subset=['Sex']))
#                                   Name PClass   Age     Sex  Survived  SexCode
# 0         Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
# 2  Allison, Mr Hudson Joshua Creighton    1st  30.0    male         0        0

# ------------drop_duplicates默认保留重复行中先出现的行，然后删除剩余的行，keep=last参数可以修改保留最后的
print(dataframe.drop_duplicates(subset=['Sex'],keep='last'))
#                     Name PClass   Age     Sex  Survived  SexCode
# 1307  Zabour, Miss Tamini    3rd   NaN  female         0        1
# 1312       Zimmerman, Leo    3rd  29.0    male         0        0
