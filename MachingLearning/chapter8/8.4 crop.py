# 裁剪图像
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_GRAYSCALE)
# 选择所有的行和前128列
image_cropped = image[:,:128]

plt.imshow(image_cropped,cmap="gray"),plt.axis("off")
plt.show()