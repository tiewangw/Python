# 移除背景:在所需的前景图像周围画一个矩形，然后运行GrabCut算法
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 加载图像并转换成RGB格式
image_bgr = cv2.imread("images/plane_256x256.jpg")
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
# 矩形的值：左上角的x坐标，左上角的y坐标，宽，高
rectangle = (0,56,256,150)
# 创建初始掩摸
mask = np.zeros(image_rgb.shape[:2],np.uint8)
# 创建grabCut函数
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
# 执行grabCut函数
cv2.grabCut(image_rgb,
            mask,
            rectangle,
            bgdModel,
            fgdModel,
            5,
            cv2.GC_INIT_WITH_RECT)
# 创建一个掩摸，将确定或很可能是背景的部分设置为0，其余的设置为1
mask_2 = np.where((mask==2) | (mask==0),0,1).astype('uint8')
# 将图像与掩摸相乘以除去背景
image_rgb_nobg = image_rgb * mask_2[:,:,np.newaxis]

# 掩摸mask
plt.imshow(mask,cmap='gray'),plt.axis("off")
# plt.show()
# 掩摸mask_2
plt.imshow(mask_2,cmap='gray'),plt.axis("off")
# plt.show()

# 显示图像
plt.imshow(image_rgb_nobg),plt.axis("off")
plt.show()





