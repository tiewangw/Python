# 将一个数值型特征离散化，分到多个离散的小区间
import numpy as np
from sklearn.preprocessing import Binarizer

age = np.array([
    [6],
    [12],
    [20],
    [36],
    [65]
])

# 方法1 ：根据阈值将特征二值化
binarizer = Binarizer(18)
print(binarizer.fit_transform(age))
# [[0]
#  [0]
#  [1]
#  [1]
#  [1]]
print("----------------")

# 方法2：根据多个阈值将数值型特征离散化
# bins参数中的每个数字表示的是每个区间的左边界，可以设置 right=True改变
print(np.digitize(age,bins=[20,30,64]))
# [[0]
#  [0]
#  [1]
#  [2]
#  [3]]

# 针对2个区间的使用scikit-learn的Binarizer
# 针对3个区间的使用Numpy的digitize
