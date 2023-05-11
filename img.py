import cv2
import numpy as np
img = cv2.imread("C:/Users/DELL/OneDrive/Desktop/photo.jpg")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#CARTOONISE
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)

#save
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitkey(0)
cv2.destroyAllWindows()

