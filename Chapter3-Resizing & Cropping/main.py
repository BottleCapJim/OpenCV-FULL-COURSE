import cv2
import numpy as np

#Python uses height then width
#Opencv uses width first then height
img=cv2.imread("Resources\wowsherk.png")
#first one is the height, second is the width, third is the channels of the image aka RGB
print(img.shape)
#For the resize function the width is put in first then the height
imgResize=cv2.resize(img,(200,150))
print(imgResize.shape)
#height first width second cropped image
#image keeps fist 100 height pixels and for width pixels between 100 and 200
imgCropped=img[0:100,100:200]

cv2.imshow("Original shrek",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)
    