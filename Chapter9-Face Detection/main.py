import cv2

##This xml file contains trained models for the detection of the cascade of the front face
##It has a model that has been trained with 1000s of images to detect the front of a face
faceCascade=cv2.CascadeClassifier("Resources\haarcascade_frontalface_default (1).xml")
img=cv2.imread("Resources\wowsherk.png")
#imgResize=cv2.resize(img,(640,480))
imgGrey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

##Detects the cascade of the face
faces=faceCascade.detectMultiScale(img,1.1,4)

for (x,y,w,h) in faces:
##Creates a rectangle around the face
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result Image",img)
cv2.imshow("Gray Image",imgGrey)
cv2.waitKey(0)