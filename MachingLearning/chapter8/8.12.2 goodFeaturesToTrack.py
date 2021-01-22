# 角点检测:检测图像角点的位置
# goodFeaturesToTrack : 确定一组固定数量的明显的角点
import cv2
import numpy as np
from matplotlib import pyplot as plt
# 加载图像
image_bgr = cv2.imread("images/plane_256x256.jpg")
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

corners_to_detect = 10  # 待检测角点的数量
minimum_quality_score = 0.05  # 角点的最差质量（0~1）
minimum_distance = 25   # 角点间的最短欧氏距离

# 检测角点
corners = cv2.goodFeaturesToTrack(image_gray,
                                  corners_to_detect,
                                  minimum_quality_score,
                                  minimum_distance)
corners = np.float32(corners)

# 在每个角点上画白圈
for corner in corners:
    x,y = corner[0]
    cv2.circle(image_bgr,(x,y),10,(255,255,255),-1)


# 转换成灰度图
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

plt.imshow(image_rgb, cmap="gray"), plt.axis("off")
plt.show()
