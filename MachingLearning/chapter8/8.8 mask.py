# 颜色分离：
# 1、将图像转换成HSV格式（H/S/V分别代表色调、饱和度、亮度）
# 2、定义要分离的一系列值
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg")
# 将BGR格式转换成HSV格式
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# 定义HSV格式中蓝色分量的区间
lower_blue = np.array([50,100,50])
upper_blue = np.array([130,255,255])
# 创建掩摸
mask = cv2.inRange(image_hsv,lower_blue,upper_blue)
# 应用掩摸
image_bgr_masked = cv2.bitwise_and(image,image,mask=mask)
# 从BGR格式转换炒年糕RGB格式
image_rgb = cv2.cvtColor(image_bgr_masked,cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb),plt.axis("off")
# plt.show()

# 只保留掩摸的白色区域
plt.imshow(mask,cmap="gray"),plt.axis("off")
plt.show()

