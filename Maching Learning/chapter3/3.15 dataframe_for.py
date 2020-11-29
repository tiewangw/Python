# 遍历数据

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

for name in dataframe['Name'][0:2]:
    print(name.upper())

# ALLEN, MISS ELISABETH WALTON
# ALLISON, MISS HELEN LORAINE