
from Adafruit_Thermal import *
printer = Adafruit_Thermal('COM5', 9600, timeout=5)

list1 = ["Summit", "Pocari", "Coke", "Gatorade", "Natures"]
list2 = [1,2,3,4,5]

printer.justify('C')
printer.println("Reverse Vendo Transaction")
printer.println("")
printer.justify('L')

for  i in range(5):
    printer.println(f"{list1[i]} ........ PHP {list2[i]}.00")