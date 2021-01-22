# 获取一个基于图像颜色的特征
import cv2
import numpy as np
from matplotlib import  pyplot as plt

# 以BGR格式加载图像
image_bgr = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_COLOR)
# 计算每个通道的平均值
channels = cv2.mean(image_bgr)
# 交换红色和蓝色通道，将图像从BGR格式转换长RGB格式
observation = np.array([channels[2],channels[1],channels[0]])
print(observation)
# [ 90.53204346 133.11735535 169.03074646]

# plt.imshow(observation),plt.axis("off")
# plt.show()
