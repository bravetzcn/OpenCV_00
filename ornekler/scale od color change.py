import cv2
img=cv2.imread('Aziz_Sancar_0060.jpg')
img=cv2.resize(img,(640,480))
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('rgb',img1)
cv2.imshow('hsv',img2)
cv2.imshow('gray',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()