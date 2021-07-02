import cv2
import numpy as np

#img = cv2.imread("image.jpg")
#cv2.imshow('input_image', img)
"""
# playing with perspective
width, height = 1250, 577
c1= [100,100]
c2= [287,188]
c3= [154,482]
c4= [352,440]

pts1 = np.float32([c1,c2,c3,c4])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img, matrix,(width,height))

cv2.imshow('',imgOut)
"""
"""
# edge detection
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(7,7),1)
canny = cv2.Canny(blur,50,50)

cv2.imshow('canny', canny)
"""
# """
# face detection
# load the cascade
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
# get video capture
cap = cv2.VideoCapture(0)
while True:
    # capture frame-by-frame
    ret, frame = cap.read()
    # mirror
    mirror = cv2.flip(frame, 1)
    # convert to gray
    gray = cv2.cvtColor(mirror, cv2.COLOR_BGR2GRAY)
    # detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(mirror, (x,y), (x+w, y+h), (0, 255, 0), 2)
    # display the frame
    cv2.imshow('frame', mirror)
    # break with 'q'
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# """

