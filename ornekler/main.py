import cv2
img=cv2.imread('unnamed.jpg')
img=cv2.resize(img,(680,480))
cv2.imshow('image',img)
cv2.imwrite('aziz_sancar.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()