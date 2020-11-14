# 创建一个仿真数据集来做分类，使用make_classification

from sklearn.datasets import make_classification
# 加载特征矩阵和目标向量
features,target = make_classification(n_samples=100,
                                      n_features=3,
                                      n_informative=3,
                                      n_redundant=0,
                                      n_classes=2,
                                      weights=[.25,.75],  # 利用weight生成不均衡的仿真数据集，%25观察值属于第一个分类，%75的观察值属于第2个分类
                                      random_state=1)

# 查看特征矩阵
print('Featrue Matrix\n' , features[:3])
# Featrue Matrix
#  [[ 1.06354768 -1.42632219  1.02163151]
#  [ 0.23156977  1.49535261  0.33251578]
#  [ 0.15972951  0.83533515 -0.40869554]]

# 查看目标向量
print('Target Vector\n' , target[:3])
# Target Vector
#   [1 0 0]



