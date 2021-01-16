# 平滑处理图像：将每个像素的值变换为其相邻像素的平均值
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_GRAYSCALE)

# 用5x5的核进行平滑操作
image_blurry = cv2.blur(image,(5,5))
plt.imshow(image_blurry,cmap="gray"),plt.axis("off")
# plt.show()

# 用100x100的核进行平滑操作
image_very_blurry = cv2.blur(image,(100,100))
plt.imshow(image_very_blurry,cmap="gray"),plt.xticks([]),plt.yticks([])
plt.show()