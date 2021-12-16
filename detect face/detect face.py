import cv2
image=cv2.imread("img1.jpg")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#greyimg=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(image,scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    imageop=cv2.rectangle(image, (x, y), (x+w,y+h), (99, 255, 3), 2)
cv2.imshow("mypic", imageop)
cv2.waitKey(4000)
cv2.destroyAllWindows()


