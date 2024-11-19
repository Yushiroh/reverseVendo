import serial
import time

ser = serial.Serial('COM6', 9600, timeout=1)


# ser.open()
# ser.close()

data = ser.read(1)

while True:

    if ser.isOpen():
        try:
            input_data = ser.readline().decode("utf-8")

                  
            if(input_data == 'A'):
                print("EYYY")
            elif(input_data == 'B'):
                print("AYY")

        except:
            print("ERROR")
    

    

    
      
     
