import cv2

img = cv2.imread("result.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #BGR2を指定

cv2.imwrite("gray_result.jpg", img_gray)