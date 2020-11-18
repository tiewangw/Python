import pandas as pd

#  使用Datframe创建一个空数据帧并定义好每一列
dataframe = pd.DataFrame()

dataframe['Name'] = ['Jacky Jackson', 'Steven Stenvenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True, False]

print(dataframe)
print('--------------------')

# 往其底部加一行
new_person = pd.Series(['Molly Monney', 40, True], index=['Name', 'Age', 'Driver'])

# 附加一行
print(dataframe.append(new_person, ignore_index=True))

#                 Name  Age  Driver
# 0      Jacky Jackson   38    True
# 1  Steven Stenvenson   25   False
# 2       Molly Monney   40    True




##########
# 在真实场景中，创建一个空的数据帧对象然后再填充数据的情况几乎不会发生。
# 一般通过加载其他源（例如一个CSV文件或数据库）的真实数据创建数据帧
