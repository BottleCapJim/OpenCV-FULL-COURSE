import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def empty(e):
    pass

#Colors values for yellow green and pink used for mask
myColors=[[32,30,0,42,255,255],[59,146,144,89,255,255],[129,63,193,179,255,255]]
#Detects forehead bruh
#myColors = [[130, 50, 50, 180, 255, 255]]

#Color values for yellow green and pink for dot
myColorValues=[[88,238,255],[80,175,76],[146,89,240]]  ##Given in BGR because it is used for cv2
myPoints= [] ##[x,y,colorId]

def findColors(img,myColors,myColorValues):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:          
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv2.inRange(imgHSV,lower,upper)    
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
           newPoints.append([x,y,count])
        count+=1
#            cv2.imshow(str(color[0]),mask)
    return newPoints



def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>5:
            cv2.drawContours(imgResult,cnt,-1,(255,0,255),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True) 
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
   for point in myPoints:
         cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)
       


while True:
    success,img=cap.read()
    imgResult=img.copy()
    newPoints =findColors(img,myColors,myColorValues)

    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

#    imgResult=cv2.bitwise_and(img,img,mask=mask)
##Hue min 32, hue max 42 for orange
##Hue max 89, Sat min 146, Val min 144 for green
##Hue min 119, sat min 46, val min 255 for pink
    cv2.imshow("Original image",img)
    cv2.imshow("Result image",imgResult)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break