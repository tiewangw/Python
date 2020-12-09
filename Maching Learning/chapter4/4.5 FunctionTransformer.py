# 对一个或多个特征进行自定义的转换
# 使用FunctionTransformer对一组特征应用一个函数
import numpy as np
from sklearn.preprocessing import FunctionTransformer
# 使用pandas的apply可以进行同样的转换
import pandas as pd

# 创建特征矩阵
featrues = np.array([
    [2,3],
    [2,3],
    [2,3]
])

#定义一个简单的函数
def add_ten(x):
    return x+10

#创建转换器
ten_trans = FunctionTransformer(add_ten)
#转换特征矩阵
print(ten_trans.transform(featrues))

# [[12 13]
#  [12 13]
#  [12 13]]

# -------------------------
# 创建数据帧
df = pd.DataFrame(featrues,columns=["feature_1","featrue_2"])
# 应用函数
print(df.apply(add_ten))

#    feature_1  featrue_2
# 0         12         13
# 1         12         13
# 2         12         13
