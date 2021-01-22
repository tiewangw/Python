# 将图像转换为机器学习算法可用的样本数据
import cv2
import numpy as np
from matplotlib import  pyplot as plt

image_gray = cv2.imread("images/plane_256x256.jpg",cv2.IMREAD_GRAYSCALE)
# 将图片尺寸转换为10x10
image_10x10 = cv2.resize(image_gray,(10,10))
# 将图像数据转换成一维向量
print(image_10x10.flatten())
# [133 130 130 129 130 129 129 128 128 127 135 131 131 131 130 130 129 128
#  128 128 134 132 131 131 130 129 129 128 130 133 132 158 130 133 130  46
#   97  26 132 143 141  36  54  91   9   9  49 144 179  41 142  95  32  36
#   29  43 113 141 179 187 141 124  26  25 132 135 151 175 174 184 143 151
#   38 133 134 139 174 177 169 174 155 141 135 137 137 152 169 168 168 179
#  152 139 136 135 137 143 159 166 171 175]

plt.imshow(image_10x10,cmap="gray"),plt.axis("off")
plt.show()