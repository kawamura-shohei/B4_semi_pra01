import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('20210704_02_0208.jpg') #鳥瞰視点画像
 
# 変換前後の対応点を設定
p_original = np.float32([[739,600], [345,294], [779,132], [1114,202]]) #鳥瞰視点画像の4点
p_trans = np.float32([[677,508], [347,597], [163,122], [522,84]]) #直下視画像の4点
 
# 変換マトリクスと射影変換
M, mask = cv2.findHomography(p_original, p_trans, cv2.RANSAC) #0:すべてのポイントを使用する通常の方法、RANSAC：RANSACベースの堅牢な方法、LMEDS：最小中央値のロバストな方法
i_trans = cv2.warpPerspective(img, M, (1280, 720)) #サイズ指定
 
cv2.imwrite("result.jpg", i_trans)
cv2.imshow("result", i_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()