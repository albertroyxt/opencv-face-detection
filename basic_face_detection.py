import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Using images other than GWB, or parameter values other than the ones below, 
# leads to spurious features being detected, or not enough features...
# The whole process is pretty sensitive to parameter values.
img = cv2.imread('images/bush.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # If the 1.07 parameter becomes 1.08 we only detect right eye (???)
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.07, 1)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

cv2.imwrite("images/detected_faces_basic.jpg", img)
cv2.imshow('img',img)
cv2.waitKey(0)

