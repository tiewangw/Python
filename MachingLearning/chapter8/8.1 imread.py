# 加载图像
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 把图像导入成灰度图 imread：将图像数据转换成Nnumpy数组
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)
# 查看图像
plt.imshow(image,cmap="gray"),plt.axis("off")
plt.show()

# 显示数据类型
# print(type(image))
# <class 'numpy.ndarray'>

# 显示图像数据
# print(image)
# [[140 136 146 ... 132 139 134]
#  [144 136 149 ... 142 124 126]
#  [152 139 144 ... 121 127 134]
#  ...
#  [156 146 144 ... 157 154 151]
#  [146 150 147 ... 156 158 157]
#  [143 138 147 ... 156 157 157]]

# 显示矩阵维度
print(image.shape)
# (2270, 3600)

# 显示第一个像素点的像素值
print(image[0,0])
# 140

# 以彩色模式加载图像 BGR ： 对应 蓝色、绿色、红色
image_bgr = cv2.imread("images/plane.jpg",cv2.IMREAD_COLOR)
# print(image_bgr[0,0])
# [195 144 111]

# 转换成RGB(红绿蓝)格式
image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb),plt.axis("off")
# plt.show()




