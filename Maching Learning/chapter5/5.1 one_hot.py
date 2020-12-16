# 对nominal型分类特征编码

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer,MultiLabelBinarizer

feature = np.array([
    ["Texas"],
    ["California"],
    ["Texas"],
    ["Delaware"],
    ["Texas"]
])
# 创建one_hot编码器
one_hot = LabelBinarizer()
print(one_hot)
# 对特征进行one_hot编码
print(one_hot.fit_transform(feature))
# [[0 0 1]
#  [1 0 0]
#  [0 0 1]
#  [0 1 0]
#  [0 0 1]]

# 查看特征的分类
print(one_hot.classes_)
# ['California' 'Delaware' 'Texas']

# 对one-hot编码进行逆转换
inv = one_hot.inverse_transform((one_hot.transform(feature)))
print(inv)
# ['Texas' 'California' 'Texas' 'Delaware' 'Texas']

print("-----------------使用pandas对特征进行one-hot编码--------------------------------")
# 创建虚拟变量
pd.get_dummies(feature[:,0])
# 创建有多个分类的特征
muticlass_feature = [("Texas","Florida"),
                     ("California","Alabama"),
                     ("texas","Florida"),
                     ("Delware","Florida"),
                     ("Texas","Alabama")
                     ]
# 创建能处理多个分类的one-hot编码
one_hot_multiclass = MultiLabelBinarizer()
# 对特征进行one-hot编码
ohm = one_hot_multiclass.fit_transform(muticlass_feature)
print(ohm)
# [[0 0 0 1 1 0]
#  [1 1 0 0 0 0]
#  [0 0 0 1 0 1]
#  [0 0 1 1 0 0]
#  [1 0 0 0 1 0]]
# 查看分类
print(one_hot_multiclass.classes_)
# ['Alabama' 'California' 'Delware' 'Florida' 'Texas' 'texas']







