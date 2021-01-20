# 图像二值化;将图像转换成仅包含黑色和白色的简化版本
# 即将强度大于某个阈值的像素设置为白色并将小于该值的像素设置为黑色
import cv2
from matplotlib import pyplot as plt

image_grey = cv2.imread("images/plane_256x256.jpg", cv2.IMREAD_GRAYSCALE)

max_output_value = 255  # 输出像素的最大值
neighborhood_size = 99
subtract_from_mean = 10

image_binarized = cv2.adaptiveThreshold(image_grey,
                                        max_output_value,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # 将像素的阈值设置为相邻像素强度的加权和
                                        cv2.THRESH_BINARY,
                                        neighborhood_size,
                                        subtract_from_mean)

# 只保留掩摸的白色区域
plt.imshow(image_binarized, cmap="gray"), plt.axis("off")
plt.show()
