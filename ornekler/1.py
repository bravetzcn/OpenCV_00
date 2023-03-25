import cv2
cap=cv2.VideoCapture(0)
file_name= 'webcam.avi'
codec=cv2.VideoWriter_fourcc('W','M','V','2')
frame_rate=20
resolution=(640,480)
output=cv2.VideoWriter(file_name,codec,frame_rate,resolution)
while 1:
    ret,frame=cap.read()
    if ret==0:
        break
    frame=cv2.flip(frame,1)
    cv2.imshow('image',frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
output.release()
cap.release()
cv2.destroyAllWindows()