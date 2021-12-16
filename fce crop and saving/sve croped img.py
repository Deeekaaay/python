import cv2
font=cv2.FONT_HERSHEY_SIMPLEX
image=cv2.imread("img1.jpg")
cv2.imshow("mypic", image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#greyimg=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(image,scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    imageop=cv2.rectangle(image, (x, y), (x+w,y+h), (99, 255, 3), 2)
    imageop2=cv2.putText(imageop, str("FACE"), (x+w//3,y+h+15),font,0.5,(125, 255, 255), 1)
cv2.imshow("mypic", imageop)
cv2.waitKey(1000)
cv2.destroyAllWindows()
cropimage=imageop[y+2:y+h-2,x+2:x+w-2]
resizeimg=cv2.resize(cropimage,(400,400))
cv2.imshow("mypic", resizeimg)
cv2.waitKey(1000)
cv2.destroyAllWindows()
cv2.imwrite("cropedimg1.jpg",resizeimg)
cv2.imwrite("cropedimg2.jpg",imageop2)
