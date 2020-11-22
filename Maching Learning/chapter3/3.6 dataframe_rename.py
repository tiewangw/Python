# 重命名列

import pandas as pd
import collections

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

result = dataframe.head(2)
print(result)
#                            Name PClass   Age     Sex  Survived  SexCode
# 1   Allison, Miss Helen Loraine    1st   2.0  female         0        1
# 0  Allen, Miss Elisabeth Walton    1st  29.0  female         1        1

# ---------------重命名列--------------------
result = dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2)
print(result)
#                            Name Passenger Class  ...  Survived SexCode
# 0  Allen, Miss Elisabeth Walton             1st  ...         1       1
# 1   Allison, Miss Helen Loraine             1st  ...         0       1


# -----------创建字典-----
column_names = collections.defaultdict(str)

for name in dataframe.columns:
    column_names[name]
print(column_names)
# defaultdict(<class 'str'>, {'Name': '', 'PClass': '', 'Age': '', 'Sex': '', 'Survived': '', 'SexCode': ''})