import cv2
import numpy as np
from PIL import Image

img = cv2.imread("result.jpg")

# 真っ黒な画素以外は白くしてマスク画像を作成
mask_pixels = (img != (0, 0, 0)).all(axis=-1)
img[mask_pixels] = (255, 255, 255)

cv2.imwrite("mask_result.jpg", img)