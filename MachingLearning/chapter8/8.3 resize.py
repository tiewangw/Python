# 调整图像大小
import cv2
from matplotlib import pyplot as plt

# 导入图像
images = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_GRAYSCALE)

# 调整为50x50像素
images_50x50 = cv2.resize(images,(50,50))
# 查看图像
plt.imshow(images_50x50,cmap="gray"),plt.axis("off")
plt.show()