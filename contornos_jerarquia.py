import cv2
import numpy as np

path="hierarchy.png"
i=1
m=3
n=3
k=np.ones((m,n),np.uint8)

img_gray=cv2.imread(path,0)


img_median = cv2.medianBlur(img_gray.copy(), 3)

ret, img_binary = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)

##aplicar filtros morfologicos##

img_dilate=cv2.dilate(img_binary.copy(), kernel = k, iterations = i)

img_erode=cv2.erode(img_binary.copy(), kernel = k, iterations = i)

contours, hierarchy = cv2.findContours(img_binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(contours, hierarchy)

cv2.imshow("img_binary",img_binary)
cv2.imshow("img_dilate",img_dilate)
cv2.imshow("img_erode",img_erode)
cv2.imshow("img_median",img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()
