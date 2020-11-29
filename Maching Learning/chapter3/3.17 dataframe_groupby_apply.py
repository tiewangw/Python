# 对所有分组应用某个函数

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

df = dataframe.groupby('Sex').apply(lambda x:x.count())

print(df)
#         Name  PClass  Age  Sex  Survived  SexCode
# Sex
# female   462     462  288  462       462      462
# male     851     851  468  851       851      851