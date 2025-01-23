import cv2 
import numpy as np 
  
  
image = cv2.imread("image.jpeg")
r = cv2.selectROI("select the area", image)

for i in range(int(r[1]), int(r[1]+r[3])):
    for j in range(int(r[0]), int(r[0]+r[2])):
        image[i][j] = [0, 0, 0]

cv2.imshow("image", image)
cv2.waitKey(0)