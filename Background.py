import cv2
# This is my webcam 
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,back=cap.read() #cap.read() #here is am simply reading
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5)==ord('q'):
            # save the image
            cv2.imwrite("image.jpeg",back)
            break
cap.release()
cv2.destroyAllWindows()
            