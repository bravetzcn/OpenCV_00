import cv2
import numpy as np
pencere=np.zeros((512,512,3),np.uint8)+255
pencere=cv2.resize(pencere,(640,480),interpolation=cv2.INTER_AREA)
#to drawing line
cv2.line(pencere,(30,90),(30,180),(0,255,0),thickness=5)
cv2.line(pencere,(30,90),(120,90),(0,255,0),thickness=5)
cv2.line(pencere,(120,90),(120,180),(0,255,0),thickness=5)
cv2.line(pencere,(30,180),(120,180),(0,255,0),thickness=5)
# to drawing rectangle
cv2.rectangle(pencere,(190,90),(360,180),(0,0,255),thickness=3)
#to drawing circle
cv2.circle(pencere,(370,400),60,(255,0,0),thickness=-1)
#to use polylines
points= np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(pencere,[points],True,(0,255,0),thickness=3)
cv2.imshow('image',pencere)
cv2.waitKey(0)
cv2.destroyAllWindows()