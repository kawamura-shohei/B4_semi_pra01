import cv2
import numpy as np
from PIL import Image

img = cv2.imread("result.jpg")

mask_pixels = (img != (0, 0, 0)).all(axis=-1)
img[mask_pixels] = (255, 255, 255)

cv2.imwrite("mask_result.jpg", img)