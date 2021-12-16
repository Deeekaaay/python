import cv2
import os
folderlist = os.listdir("input")
f = 1
for filename in folderlist:
    image = cv2.imread("input/" + filename)
resizeimg = cv2.resize(image, (200, 200))
cv2.imshow("mypic", resizeimg)
cv2.waitKey(500)
cv2.destroyAllWindows()
cv2.imwrite("output/resized image " + str(f) + ".jpg", resizeimg)