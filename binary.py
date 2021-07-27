import cv2
import numpy as np

img = cv2.imread("gray_result.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #BGR2を指定してグレースケール化
ret2, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU) #大津の二値化
print("ret: {}".format(ret2)) #閾値表示

kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
], dtype=np.uint8)
img_delation = cv2.dilate(img_binary, kernel, iterations=3)
img_erosion = cv2.erode(img_delation, kernel, iterations=3)
#closing = cv2.morphologyEx(img_binary, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("binary_result.jpg", img_erosion)