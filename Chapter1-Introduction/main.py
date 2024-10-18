import cv2
##Double hashtags are for comments a singular hastag is for actual code
##The variable img is gonna use a function in cv2 which reads the image and the parameter of the function witholds the path of
##the image
#img=cv2.imread("Resources\wowsherk.png")
##The function imshow displays the image and the first argument is the name of the window and the second argument is the image
#cv2.imshow("HAHASHAWSHANK", img)
##The function waitKey is the time the image is displayed in miliseconds and if you put in 0 it shows indefinitely
#cv2.waitKey(0)

##The object cap is used to store the video file using the method cv2.VideoCapture
#cap=cv2.VideoCapture("Resources\WIN_20220506_19_02_26_Pro.mp4")
##0 as a parameter accesses the first webcam and if you have 2 webcams you use 1 excetera
cap=cv2.VideoCapture(0)
##Id number 3 is for the width
cap.set(3,640)
##Id number 4 is for the height
cap.set(4,480)
##Id number 10 is for the brightness so it doesn't look atrocious
cap.set(10,100)
##A while loop is used because the image is only displayed for 1 milisecond and then breaks and therefore this displays it
##indefinetely
while True:
##success is a boolean value used to show whether the image was displayed correctly if it has then it outputs true
##cap.read() is stored in img(also success), this stores the next frame for every iteration of the while loop
    success,img=cap.read()
    cv2.imshow("Video",img)
##the key needs to be presssed for 1 millisecond, the operator & is used instead of and because you need to compare the binary
##or compares the binary ascii value of the word q, ord function gets the ascii value of the  word q 
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break