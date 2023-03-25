import cv2
img=cv2.imread('Aziz_Sancar_0060.jpg')
img=cv2.resize(img,(640,480))
roi=img[30:350,150:500]

boyut=img.shape
print(boyut)
color=img[300,400]
b=img[300,400,0]
g=img[300,400,1]
r=img[300,400,2]
print(color)
print(b)
print(g)
print(r)
green=img.item(300,400,1)
print(green)
img.itemset((300,400,1),180)
print(img[300,400,1])
cv2.imshow('image',img)
cv2.imshow('Roi',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()