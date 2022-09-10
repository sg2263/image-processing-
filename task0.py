import cv2 ##before importing this package we need to install opencv in our system ,achieved by pip install opencv-python in cmd
## download harcascade functions, here we use the frontal_face function

faceCascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) ##0 means selecting defalt video source ,which would be my webcam

## when we read video it is inform of stream of individual images , so if we dont initiate a look our frame will stop only for one moment (one image / snap)and not in form of live video
while True: 
    flag,frame = cap.read()
    
    
    cv2.imshow('frame',frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray,1.1,5)
    
    for (a,b,c,d)in faces://a and b are starting pt and c and d are length 
        cv2.rectangle(frame,(a,b),(a+c,b+d),(255,0,0),2) 
        
   
    
    k=cv2.waitKey(30) & 0xff ##data capture is so fast each subsequent image is overiding the next image so we need waitKey() method, it will wait for 30 milisecond before it goes to the next picture
    if k==ord(q):## returns unicode value of character 
    break
        
        
cap.release()//outside while 