# 创建一个适合做聚类处理的数据集 ，使用make_blobs

from sklearn.datasets import make_blobs

# 加载特征矩阵和目标向量
features, target = make_blobs(n_samples=100,
                              n_features=2,
                              centers=3, # centers参数决定了要生成多少个聚类
                              cluster_std=0.5,
                              shuffle=True,
                              random_state=1)

# 查看特征矩阵
print('Featrue Matrix\n', features[:3])
# Featrue Matrix
# [[ -1.22685609   3.25572052]
#  [ -9.57463218  -4.38310652]
# [-10.71976941  -4.20558148]]

# 查看目标向量
print('Target Vector\n', target[:3])
# Target Vector
#    [0 1 1]


print("-----------------------------")

# matplotlib 能将make_blobs生成的聚类可视化地显示出来
import matplotlib.pyplot as plt

# 查看散点图
plt.scatter(features[:,0], features[:,1],c=target)
plt.show()