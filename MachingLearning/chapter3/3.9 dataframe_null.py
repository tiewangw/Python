# 筛选出数据帧中的缺失值

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe[dataframe['Age'].isnull()].head(2))
#                             Name PClass  Age     Sex  Survived  SexCode
# 12  Aubert, Mrs Leontine Pauline    1st  NaN  female         1        1
# 13      Barkworth, Mr Algernon H    1st  NaN    male         1        0

#   pandas没有实现NaN,使用Numpy的NaN来表示缺失值。

# 用NaN替换一些值
dataframe['Sex'] = dataframe['Sex'].replace('male',np.nan);
print(dataframe['Sex'].unique())    # ['female' nan]