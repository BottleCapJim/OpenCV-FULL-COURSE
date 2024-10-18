import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("Resources\wowsherk.png")
##he image is converted to grey scale and in opencv you use BGR instead of RGB
##The method cv2Color is used to change an images color
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##GaussianBlur is used to make the image blurry, and the second value in the paranthesis
##is used to define the matrix of the image, as for the last one, google/GPT it yourself
##actually matrix might also just control how blurry the image is and the number is usually odd
imgBlur=cv2.GaussianBlur(imgGrey,(7,7),0)
##The Canny function shows the number of edges in an image respective of the threshold value
##If a pixels value is lower than the lower threshold which is the first one it is considered
##to be a non-edge and is not included in the final image, if it is above it is included and
##if they are in the middle the ones with a higher pixel value are more likely to be included
imgCanny=cv2.Canny(img,150,200)
##This makes the edges thicker
imgDilute=cv2.dilate(imgCanny,kernel,iterations=1)
##This makes the edges thinner
imgEroded=cv2.erode(imgDilute,kernel,iterations=1)
cv2.imshow("GreyImage",imgGrey)
cv2.imshow("BlurImage",imgBlur)
cv2.imshow("CannyImage",imgCanny)
cv2.imshow("DilutedImage",imgDilute)
cv2.imshow("ErodedImage",imgEroded)
cv2.waitKey(0)