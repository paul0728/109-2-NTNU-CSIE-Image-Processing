import numpy as np
import cv2

#呼叫分類器
face_cascade = cv2.CascadeClassifier('D:\\Anaconda3\\pkgs\\libopencv-4.0.1-hbb9e17c_0\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\\Anaconda3\\pkgs\\libopencv-4.0.1-hbb9e17c_0\\Library\\etc\\haarcascades\\haarcascade_eye.xml')

img = cv2.imread('C:\\Users\\paul\\Downloads\\y.jpg',cv2.IMREAD_REDUCED_COLOR_2)
#img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	#cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
retval=cv2.imwrite('C:\\Users\\paul\\Desktop\\face_detection.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()