# 创建一组特征来表示图像中的颜色
import cv2
import numpy as np
from matplotlib import  pyplot as plt

# 以BGR格式加载图像
image_bgr = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_COLOR)
# 将图像转换成RGN
image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB)
# 创建一个特征列表
features = []

# 为每一个颜色通道计算直方图
colors = ["r","g","b"]
# 为每一个通道计算直方图，并将它加入特征列表中
for i ,channel in enumerate(colors):
    histogram = cv2.calcHist([image_rgb], # 图像
                             [i], # 颜色通道的序号
                             None, # 不使用掩摸
                             [256], # 直方图的尺寸
                             [0,256]) # 范围
    features.extend(histogram)

observation = np.array((features)).flatten()

print(observation[0:5])
# [1008.  217.  184.  165.  116.]


# 为每一个通道计算直方图，并将它加入特征列表中
for i ,channel in enumerate(colors):
    histogram = cv2.calcHist([image_rgb], # 图像
                             [i], # 颜色通道的序号
                             None, # 不使用掩摸
                             [256], # 直方图的尺寸
                             [0,256]) # 范围
    plt.plot(histogram,color = channel)
    plt.xlim([0,256])

plt.show()



