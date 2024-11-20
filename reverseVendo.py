import numpy as np
import torch
import cv2 as cv
import serial
import time
from ultralytics import YOLO
from Adafruit_Thermal import *

printer = Adafruit_Thermal('COM5', 9600, timeout=5)
ser = serial.Serial('COM6', 9600, timeout=1)
data = ser.read(1)

model = YOLO('petbottlesv8_v1.pt')

classesOrigin = ["natures", "pocari", "summit", "coke", "gatorade"]

transactList = []
listPrices = []

class_labels = model.names if hasattr(model, 'names') else ['class_0', 'class_1', 'class_2'] 
cap = cv.VideoCapture(0)
# img = cv.imread("PetBottles\SUMMIT\IMG_9745.JPG")

if not cap.isOpened():
    print("Cannot open camera")
    exit()

def receiptMake():
    printer.justify('C')
    printer.println("Reverse Vendo Transaction")
    printer.println("")
    printer.justify('L')

    for  i in range(5):
        printer.println(f"{transactList[i]} ........ PHP {listPrices[i]}.00")

def appender(itemDetected):

    print("Function Entered!")

    if itemDetected == classesOrigin[0]:
        transactList.append("Natures")
        listPrices.append(5)
    elif itemDetected == classesOrigin[1]:
        transactList.append("Pocari")
        listPrices.append(10)
    elif itemDetected == classesOrigin[2]:
        transactList.append("Summit")
        listPrices.append(15)
    elif itemDetected == classesOrigin[3]:
        transactList.append("Coke")
        listPrices.append(20)
    elif itemDetected == classesOrigin[4]:
        transactList.append("Gatorade")
        listPrices.append(25)
    else:
        print("Else baby")

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
                results = model(frame)
                print("EYYY")
                for result in results:
                    global currentItem
                    class_id = result.probs.top1   
                    confidence = result.probs.top1conf.item()  
                    label = class_labels[class_id] 
                    print(f"Class detected: {label}")
                    currentItem = label
                    cv.putText(frame, f"{label} {confidence:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                print(currentItem)
                appender(currentItem)
                print(f"list: {transactList} / price: {listPrices}")

                cv.imshow('Captured Image - Classification Result', frame)



            elif(input_data == 'B'):
                print("AYY")
                if len(transactList) > 0:
                    receiptMake()
                    transactList.clear()
                    listPrices.clear()
                else:
                    print("no list!")

        except Exception as e:
            print(e)


    if cv.waitKey(1) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()