# 保存图像
import cv2

image = cv2.imread("images/plane.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imwrite("images/plane_2021.jpg",image)