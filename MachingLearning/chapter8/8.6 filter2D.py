# 对图像进行锐化处理：突出显示目标像素的核
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_GRAYSCALE)
# 创建核
kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
# 锐化图像
image_sharp = cv2.filter2D(image,-1,kernel)

plt.imshow(image_sharp,cmap="gray"),plt.axis("off")
plt.show()










