# 对一个特征进行转换，使其平均值为0，标准差为1
# scikit-learn 的Standardcaler能同事执行这两个转换
import numpy as np
from sklearn import preprocessing
# 创建特征
x = np.array([
    [-1000.1],
    [-200.2],
    [-500],
    [-9000.9]
])

# 创建缩放器
scaler = preprocessing.StandardScaler()
# 特征转换
standardized = scaler.fit_transform(x)

print(standardized)

# [[ 0.45729902]
#  [ 0.67565712]
#  [ 0.5938172 ]
#  [-1.72677335]]

print("Mean",round(standardized.mean()))   # Mean -0.0
print("Standard deviation",standardized.std()) # Standard deviation 1.0


