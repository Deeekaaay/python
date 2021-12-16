import cv2
print("hello there")
print(''' 
purple box are eyes
green box is face
enter Q to quit..!''')
font=cv2.FONT_ITALIC
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
        cropimage = imageop[y + 2:y + h - 2, x + 2:x + w - 2]
        resizeimg = cv2.resize(cropimage, (600, 600))
    for x1,y1,w1,h1 in eye:
        imageop2 =cv2.rectangle(imageop, (x1, y1), (x1+w1,y1+h1), (255, 3, 188), 2)
        imageop3=cv2.putText(imageop, str("dinesh"),(x+w//3,y+h+15),font,0.5,(125, 255, 255),2)
        cv2.imwrite("dinesh data/dinesh" + str(a) + ".jpg", resizeimg)
        m=0
        cv2.imshow("vid", imageop3)
    key=cv2.waitKey(100)
    if key==ord("q"):
        break
    a=a+1
video.release()
cv2.destroyAllWindows()
m=m+1
print("your data is stored in the given folder totally")
print(a)

