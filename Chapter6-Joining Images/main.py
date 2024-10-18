##It's hard to manage a ton of images so I will be putting all of them together in one window
import cv2
import numpy as np
img=cv2.imread("Resources\wowsherk.png")
#the function hstack in numpy is used to stack images on horizontally, they must be in 2 sets of brackets
imgHor=np.hstack((img,img,img))
##Same thing but instead of stacking horizontally it stacks the images vertically
##A problem with these methods is that you cannot resize the image(so they may overlap) and another problem is that if the
##images don't have the same number of channels aka(RBG,Grey scale) then the method will not work
imgVert=np.vstack((img,img,img))
cv2.imshow("Horizontally Stacked Image",imgHor)
cv2.imshow("Vertically Stacked Image",imgVert)
##cv2.imshow("Shrek",img)
cv2.waitKey(0)