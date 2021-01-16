# 提升对比度
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_GRAYSCALE)
image_enhanced = cv2.equalizeHist(image)

# 增强图像
plt.imshow(image_enhanced,cmap="gray"),plt.axis("off")
# plt.show()

#    ----对彩色图像进行增强操作-----
image_bgr = cv2.imread("images/plane.jpg")
# 转换成YUV格式
image_yuv = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2YUV)
# 对图像应用直方图均衡
image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:,:,0])
# 转换成RGB格式
image_rgb = cv2.cvtColor(image_yuv,cv2.COLOR_YUV2BGR)

plt.imshow(image_rgb),plt.axis("off")
plt.show()

