import cv2
cap=cv2.VideoCapture(0)
nPlateCascade=cv2.CascadeClassifier("Resources\haarcascade_russian_plate_number.xml")
count=0
minArea=200
color=(255,0,255)

while True:
    success,img=cap.read()

    imgGrey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    nPlate=nPlateCascade.detectMultiScale(img,1.1,4)

    for (x,y,w,h) in nPlate:
        area=w*h
        if area>minArea:
           cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
           cv2.putText(img,"Number Plate",(x,y-5),1,cv2.FONT_HERSHEY_COMPLEX_SMALL,color,2)
           imgRoi=img[y:y+h,x:x+w]
           cv2.imshow("Region of Interest",imgRoi)

    cv2.imshow("Original image",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
##Writes the image to the Scanned folder
##Tho this rewrites everything so rip previous scans :(
        cv2.imwrite("Resources\\Scanned\\NoPlate_"+str(count)+".jpg",imgRoi)
        count+=1
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break