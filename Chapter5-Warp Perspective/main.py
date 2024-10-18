import cv2
import numpy as np

img=cv2.imread("Resources\inretrospect.jpeg")
width,height=300,300
#(upper left510,320),(upper right640,226),(bottom right640,334),(bottom left510,440)
pts1=np.float32([[510,320],[640,226],[510,440],[640,334]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])    
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Warped Image",imgOutput)
cv2.imshow("Original image",img)
cv2.waitKey(0)