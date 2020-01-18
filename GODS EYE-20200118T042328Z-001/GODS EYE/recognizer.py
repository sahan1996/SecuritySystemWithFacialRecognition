# -*- coding: utf-8 -*-
"""
Created on Fri May 18 02:51:47 2018

@author: Sahan
"""

import cv2
import numpy as np
import serial
import time
arduinoData=serial.Serial('com10',9600)

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read('trainner/trainingData.yml')
id=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(conf<50):
             if(id==1):
                 id='Thaththa'
                 arduinoData.write('y'.encode())
             elif(id==2):
                id='amma'
                arduinoData.write('y'.encode())
             elif(id==3):
                id='Sahan'
                arduinoData.write('y'.encode())
             
            
        else:
                id='unknown'
                arduinoData.write('n'.encode())
            
       
        cv2.putText(img,str(id),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
    cv2.imshow("face",img);
    if(cv2.waitKey(1)==ord("q")):
        break;
arduinoData.close()        
cam.release()
cv2.destroyAllWindows()
