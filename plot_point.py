import cv2

img = cv2.imread(f"Wiki.jpg")
img_copy = img.copy()

cv2.circle(img_copy, (677, 508), 10, (0, 0, 255), thickness=-1)
cv2.circle(img_copy, (347, 597), 10, (0, 0, 255), thickness=-1)
cv2.circle(img_copy, (163, 122), 10, (0, 0, 255), thickness=-1)
cv2.circle(img_copy, (522, 84), 10, (0, 0, 255), thickness=-1)

cv2.imwrite("result_point.jpg", img_copy)