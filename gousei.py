from PIL import Image, ImageDraw

img1 = Image.open('Wiki.jpg')
img2 = Image.open('result.jpg')
back_im = img1.copy()

# マスク画像読み込み
mask = Image.open('mask_result.jpg').convert("L")

# マスク画像を基に貼り合わせ
back_im.paste(img2, (0, 0), mask)

back_im.save("registration_result.jpg")