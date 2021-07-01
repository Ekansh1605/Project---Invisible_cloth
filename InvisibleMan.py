import cv2                         ## What is HSV:- HU represent the color S represents saturation what amout of colour is mixed with white color
import numpy as np                 #### V value represents how much color is mixed with the black color
cap=cv2.VideoCapture(0)            ### HSV describes the color that how we see the color from the eyes that is human eyes and how much light intensity is 
back=cv2.imread('./image.jpeg')    ### projected on the object
while cap.isOpened():              ### RGB describes thecolor of combinations of color..
    #take each frame
    ret,frame=cap.read()
    if ret:
        # How do we convert RGB to HSV?
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        # How to get the HSV Value?
        # lower: hue - 10,100,100,higher: hue + 10,255,255
        red=np.uint8([[[0,0,255]]])
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #print(hsv_red) ## after seeing this i come to know that i have the hsv value of red color..
        
        #Threshold the value to get only red colors
        l_red=np.array([0,100,20])
        u_red=np.array([10,255,255])
        #l=np.array([160,100,20])
        #u=np.array([179,255,255])
        
        mask=cv2.inRange(hsv,l_red,u_red)
        #mask1=cv2.inRange(hsv,l,u)
        #cv2.imshow("mask",mask)
        #full_mask=mask1+mask
        ## All things red
        part1=cv2.bitwise_and(back,back,mask=mask)
        #cv2.imshow("part1",part1)
        
        mask=cv2.bitwise_not(mask)
        
        ## part 2 is all things not red
        part2=cv2.bitwise_and(frame,frame,mask=mask)
        #cv2.imshow("mask",part2)
        
        cv2.imshow("invisibleMan",part1+part2)
        if cv2.waitKey(5)==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()