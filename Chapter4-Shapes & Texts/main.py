import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#print(img)
##The colors that are assigned are based on RGB
##The first one is used for height and the next one is used for width
##The height is defined from top down, not bottom up, these are the thresholds
img[400:500,100:300]=0,255,0
##if you don't use thresholds then the whole image is that specific color
#img[:]=0,255,0
#cv2.line(img,(0,0),(300,300),(0,0,255),3)
#This is used for the whole image, first parameter is starting place
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
##Second parameter is the top left corner and the third parameter is the bottom right corner
##together the diagonal area is used to determine how big it is(last parameter is thickness)
#cv2.rectangle(img,(150,200),(250,350),(0,255,255),3)
cv2.rectangle(img,(300,100),(500,300),(0,255,255),cv2.FILLED)   
##Second parameter is the center and the third parameter is the radius
cv2.circle(img,(400,50),30,(0,255,0),5)
##Second parameter is the text, third is position, fourth is font(obvious), fifth is scale,
##sixth is color, last one is thickness, difference between scale and thickness is
##scale is strech thickness is THICCNESS, scale can be in integer or decimal
cv2.putText(img,"Felicia Hardy>Black Cat",(50,100),cv2.FONT_ITALIC,0.5,(255,255,0),3)
cv2.imshow("Black Image", img)
cv2.waitKey(0)