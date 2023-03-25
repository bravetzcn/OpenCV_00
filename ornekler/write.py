import cv2
import numpy as np
image=np.zeros((720,1280,3),np.uint8)+255
font_1=cv2.FONT_HERSHEY_SIMPLEX
write="If you want to go big, stop thinking small."
cv2.putText(image,write,(10,30),font_1,1,(0,0,0),1,cv2.LINE_AA)

cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()