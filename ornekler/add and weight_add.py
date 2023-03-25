import cv2
img1=cv2.imread('Aziz_Sancar_0060.jpg')
img2=cv2.imread('iJDUPAUO.jpg')
img1=cv2.resize(img1,(640,480))
img2=cv2.resize(img2,(640,480))
#we used to add function
collect=cv2.add(img1,img2)
#we used to addWeighted fonction
weight=cv2.addWeighted(img1,0.7, img2,0.3,0)
cv2.imshow('COL',collect)
cv2.imshow('Weg',weight)
cv2.waitKey(0)
cv2.DestroyAllWindows()

