import numpy as np
import cv2 as cv
import serial
import time

ser = serial.Serial('COM6', 9600, timeout=1)
data = ser.read(1)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
 
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)

    if ser.isOpen():
        try:
            input_data = ser.readline().decode("utf-8")

                  
            if(input_data == 'A'):
                print("EYYY")
                cv.imshow('Captured Image - Classification Result', frame)
            elif(input_data == 'B'):
                print("AYY")

        except:
            print("ERROR")


    if cv.waitKey(1) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()