import cv2 
import numpy as np

cap=cv2.VideoCapture(0)

def preProcessing(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,150,150)
    kernel=np.ones((5,5))
##Dialation of image has been done in case there are any shadows over the image which might not let it detect properly
    imgDilate=cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres=cv2.erode(imgDilate,kernel,iterations=1)
    return imgThres

def getContours(img):
    biggest=np.array([])
    maxArea=0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
#        print(area)
        if area>5000:
#            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxArea and len(approx) ==4:
                biggest=approx
                maxArea=area
##since biggest is the 4 largest approximated points which are the corners of the largest contour
##This function draws contours on the 4 approximated points          
                cv2.drawContours(imgContour,biggest,-1,(255,0,0),8)
    return biggest

def getWarp(img,biggest):
    if len(biggest) != 4:
        return img
    width,height=700,700
    pts1=np.float32(biggest)
    pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])    
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput=cv2.warpPerspective(img,matrix,(width,height))
    imgCropped=imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped=cv2.resize(imgCropped,(640,720))
    return imgCropped


while True:
    success,img=cap.read()
    imgThres=preProcessing(img)
    imgContour=img.copy()
    biggest=getContours(imgThres)
    imgWarped=getWarp(img,biggest)
    imgWarpedFlipped = cv2.flip(imgWarped, 1)

    cv2.imshow("Warped Image", imgWarpedFlipped)
    cv2.imshow("Result image",imgContour)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break