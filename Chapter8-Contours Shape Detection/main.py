import cv2
import numpy as np

def getContours(img):
##RETR_EXTERNAL retrieves the extreme outer contours, this is good for outer contours
##CHAIN_APPROX_NONE gets all the contours thet are found my the retrival function, this leaves no exception
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
##Loops through all the contours and finds their areas
    for cnt in contours:
##contourArea finds the area of the specific contour for each loop
        area=cv2.contourArea(cnt)
        print(area)
##The if statement is used to remove all the noise from the image and create a criteria for what is a shape
##and what is not
        if area>5:
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)

            if objCor==3:objectType="Tri"

            elif objCor==4:
                aspectRatio=w/float(h)
                if aspectRatio>0.95 and aspectRatio<1.05:
                    objectType="Square"
                else:
                    objectType="Rectangle"
##Not sure how to distinguish polygon from a right angled triangle
            elif objCor==6:objectType="R Triangle"

            elif objCor>6:objectType="Circle"

            else:
                objectType="None"


            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,
                        (0,255,0),2)




path="Resources\shapes.jpg"
img=cv2.imread(path)
imgContour=img.copy()


imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGrey,(7,7),1)
imgCanny=cv2.Canny(imgGrey,50,150)
imgBlank=np.zeros_like(img)

for i in range(0,1):
    cv2.imshow("Original image", img)
    cv2.imshow("Grey Image",imgGrey)
    cv2.imshow("Blur Image",imgBlur)

    getContours(imgCanny)

    cv2.imshow("Contour Image",imgContour)
    cv2.imshow("Canny Image",imgCanny)
    cv2.imshow("Blank Image",imgBlank)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        break