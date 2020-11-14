# 加载已有的样本数据集

# scikit-learn 中预制了大量的流行数据集可供使用
# scikit-learn中比较流行的玩具数据集有：
#   loan_boston ：包含了503个波士顿放假的观察值，这是一个用于研究回归算法的优质数据集。
#   loan_iris   ：包含了150个鸢尾花尺寸的观察值，这是一个用于研究分类算法的数据集。
#   loan_digits ：包含1797个手写数据图片的观察值，这是一个用于研究图像分类算法的数据集。

# 加载scikit-learn的数据集
from sklearn import datasets
# 加载手写数字数据集
digits = datasets.load_digits()
# 创建特征矩阵
features = digits.data
# 创建目标向量
target = digits.target
# 查看第一个样本数据
print(features[0])


