# 自动选择需要保留的最优特征：递归式特征消除
import warnings
from sklearn.datasets import make_regression
from sklearn.feature_selection import RFECV
from sklearn import datasets, linear_model
# 忽略一些烦人但无害的警告信息
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
# 生成特征矩阵，目标向量以及系数
features, target = make_regression(n_samples=10000,
                                   n_features=100,
                                   n_informative=2,
                                   random_state=1)
# 创建线性回归对象
ols = linear_model.LinearRegression()
# 递归消除特征
rfecv = RFECV(estimator=ols, step=1, scoring="neg_mean_squared_error")
rfecv.fit(features, target)
# print(rfecv.transform(features))
# [[ 0.00850799  0.7031277 ]
#  [-1.07500204  2.56148527]
#  [ 1.37940721 -1.77039484]
#  ...
#  [-0.80331656 -1.60648007]
#  [ 0.39508844 -1.34564911]
#  [-0.55383035  0.82880112]]

# 最优特征的数量
print(rfecv.n_features_)
# 2

# 哪些特征是最优特征
print(rfecv.support_)
# [False False False False False  True False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False  True False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False]

# 将特征从最好（1）到最差排序
print(rfecv.ranking_)
# [82 84 74 33 81  1 18 46 57 67 45  7 58 52 78  8  5 73 31 11 43 14 34 83
#  21 96 20 41 94 90 71 47 30 27 89 50 25 69 86  1 76 19 97 88  9 16 23 80
#  75 54 91 12 65 59 24 32  4 26 10 42 72  2 87 40 66  3 92 17 39 35 13 79
#  38  6 53 60 22 61 28 95 93 36 99 48 51 68 37 70 15 98 56 29 44 63 49 64
#  77 85 55 62]