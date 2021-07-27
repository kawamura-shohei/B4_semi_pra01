import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw

def main():
    mask()
    gousei()

# 射影変換
def homography():
    img_in = cv2.imread('20210704_02_0208.jpg') #鳥瞰視点画像

    # 変換前後の対応点を設定
    p_original = np.float32([[739,600], [345,294], [779,132], [1114,202]]) #鳥瞰視点画像の4点
    p_trans = np.float32([[677, 508], [347, 597], [163, 122], [522, 84]]) #直下視画像の4点

    # 変換マトリクスと射影変換
    M, mask = cv2.findHomography(p_original, p_trans, cv2.RANSAC) #0:すべてのポイントを使用する通常の方法、RANSAC：RANSACベースの堅牢な方法、LMEDS：最小中央値のロバストな方法
    img_trans = cv2.warpPerspective(img_in, M, (1280, 720)) #サイズ指定

    cv2.imwrite("result_homography.jpg", img_trans)
    return img_trans

# マスク画像作成
def mask():
    # グレースケール化
    img_gray = cv2.cvtColor(homography(), cv2.COLOR_BGR2GRAY) #BGR2を指定
    cv2.imwrite("result_gray.jpg", img_gray)

    ret2, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU) #大津の二値化
    print("ret: {}".format(ret2)) #閾値表示
    cv2.imwrite("result_binary.jpg", img_binary)

    #膨張10回、収縮10回で穴を消す
    kernel = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    ], dtype=np.uint8)
    img_delation = cv2.dilate(img_binary, kernel, iterations=10)
    img_erosion = cv2.erode(img_delation, kernel, iterations=10)
    cv2.imwrite("result_mask.jpg", img_erosion)

    return img_erosion

def gousei():
    img_background = Image.open('Wiki.jpg')
    img_registration = Image.open('result_homography.jpg')
    img_copy = img_background.copy()

    # マスク画像読み込み
    img_mask = Image.open('result_mask.jpg').convert("L")

    # マスク画像を基に貼り合わせ
    img_copy.paste(img_registration, (0, 0), img_mask)

    img_copy.save("result_registration.jpg")

if __name__ == '__main__':
        main()
