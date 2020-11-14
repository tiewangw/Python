# 用一个仿真数据集来做线性回归，使用make_regression

from sklearn.datasets import make_regression
# 加载特征矩阵，目标向量以及模型的系数
features,target,coefficients = make_regression(n_samples=100,
                                               n_features=3,
                                               n_informative=3,  # 用于确认生成目标向量的特征的数量
                                               n_targets=1,
                                               noise=0.0,
                                               coef=True,
                                               random_state=1
                                               )
# 查看特征矩阵
print('Featrue Matrix\n' , features[:3])
# Featrue Matrix
#  [[ 1.29322588 -0.61736206 -0.11044703]
#  [-2.793085    0.36633201  1.93752881]
#  [ 0.80186103 -0.18656977  0.0465673 ]]

# 查看目标向量
print('Target Vector\n' , target[:3])
# Target Vector
#  [-10.37865986  25.5124503   19.67705609]