# 将一个字典转换成一个特征矩阵
from sklearn.feature_extraction  import DictVectorizer
import pandas as pd

# 创建一个字典
data_dict = [{"Red":2,"Blue":4},
             {"Red":4,"Blue":3},
             {"Red":1,"Yellow":2},
             {"Red":2,"Yellow":2}
             ]

# 创建字典向量化器
dictvectorizer = DictVectorizer(sparse=False)
# 将字典转换成特征矩阵
features = dictvectorizer.fit_transform(data_dict)

print(features)
# [[4. 2. 0.]
#  [3. 4. 0.]
#  [0. 1. 2.]
#  [0. 2. 2.]]


# 获取特征的名字
features_names = dictvectorizer.get_feature_names()
print(features_names)
# ['Blue', 'Red', 'Yellow']


# 从特征中创建数据帧
print(pd.DataFrame(features,columns=features_names))
#    Blue  Red  Yellow
# 0   4.0  2.0     0.0
# 1   3.0  4.0     0.0
# 2   0.0  1.0     2.0
# 3   0.0  2.0     2.0
