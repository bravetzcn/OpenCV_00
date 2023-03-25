import cv2
import numpy as np
def nothing(x):
    pass

image=np.zeros((640,480,3),np.uint8)
cv2.namedWindow('img')
cv2.createTrackbar('R','img',0,255,nothing)
cv2.createTrackbar('G','img',0,255,nothing)
cv2.createTrackbar('B','img',0,255,nothing)
switch= '0:off 1:on'
cv2.createTrackbar('switch','img',0,1,nothing)

while (1):
    cv2.imshow('img',image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R', 'img')
    g = cv2.getTrackbarPos('G', 'img')
    b = cv2.getTrackbarPos('B', 'img')
    s = cv2.getTrackbarPos('switch', 'img')

    if s==0:
        image[:]=0
    else:
        image[:]=[b,g,r]

cv2.destroyAllWindows()