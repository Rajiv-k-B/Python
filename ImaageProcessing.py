# from PIL import Image

# =============================================================================
# img=Image.open("flip.png")
# 
# transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
# 
# transposed_img.save('corrected.png')
# print("done Flipping")
# =============================================================================
#  Image Enhancement
import cv2

img=cv2.imread('low.jpg')

# Prepareation for CLAHE

clahe=cv2.createCLAHE()

# Convert to gray scale image

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply enhancement

enh_img=clahe.apply(gray_img)

cv2.imwrite('enhanced.png',enh_img)

print('Done Enhancing')