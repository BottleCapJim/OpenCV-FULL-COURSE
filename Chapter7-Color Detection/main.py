import cv2
import numpy as np
##Placeholder function
def empty(e):
    pass


img=cv2.imread("Resources\wowsherk.png")
#This creates a window called track bar
#Then the window is resized to a respectable height and width for understanding
#Then 6 track bars are created in the window using the method createTrackbar which will be used to
#control the hue, saturation and value of the image to control the color detection
#The hue color values range from 0 to 170 while saturation and while range from 0 to 255
##The first argument in the parameter is for the name of the trackbar while the second is to
##refer to the window in which the track bar will be created
##the last parameter is there because I'm not sure, it just needs a function search it up
##the parameters which are integers are used to declare the lower and upper values of the trackbar
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,480)
cv2.createTrackbar("Hue Min","TrackBars",20,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

##This code has been put in a continuous loop to continuously get the 6 values and change the color of
##the image in real time
##the image is converted to get the 3 attributes which the image consists of which are hue saturation
##and value, the function getTrackbarPos is used to get the values of the trackbars as they change in real time
while True:
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hue_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    hue_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    sat_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    sat_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    val_min=cv2.getTrackbarPos("Val Min","TrackBars")
    val_max=cv2.getTrackbarPos("Val Max","TrackBars")

##hue min 23
##This outputs all the values in 1 line
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
##lower contains an array which has the lower values of HSV, these are got based on the trackbar position
    lower=np.array([hue_min,sat_min,val_min])
##upper contains an array which has the upper values of HSV, these are got based on the trackbar position
    upper=np.array([hue_max,sat_max,val_max])
#mask creates a mask or blueprint type image of imgHSV which is based on the changing lower and upper values of the trackbar position
    mask=cv2.inRange(imgHSV,lower,upper)    
##Gets rid of everything except shrek
##Ignores all the 0 pixels(black pixels) and includes the 1 pixels(white pixels) which both mask and img share
##bitwise_and creates an image with the bits(pixels) which both img and mask have in common
##This colors the image
    imgResult=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original image",img)
    cv2.imshow("HSV image",imgHSV)
    cv2.imshow("Masked Image",mask)
    cv2.imshow("Final Result Image",imgResult) 
##Using 1 because it's in a loop
##It's continuous
    cv2.waitKey(1)