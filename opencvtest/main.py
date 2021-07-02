import cv2

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
