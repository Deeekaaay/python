import cv2
print("hello there")
print(''' 
purple box are eyes
green box is face
enter q to quit..!''')
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
a=1
while True:
    check, frame=video.read()
    greyimg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(greyimg,scaleFactor=1.05, minNeighbors=5)
    eye=eye_cascade.detectMultiScale(greyimg,scaleFactor=1.05, minNeighbors=5)
    for x,y,w,h in faces:
        imageop =cv2.rectangle(frame, (x, y), (x+w,y+h), (99, 255, 3), 2)
    for x1,y1,w1,h1 in eye:
        imageop2 =cv2.rectangle(imageop, (x1, y1), (x1+w1,y1+h1), (255, 3, 188), 2)
    cv2.imshow("vid", imageop2)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    a=a+1
video.release()
cv2.destroyAllWindows()
print(a)
