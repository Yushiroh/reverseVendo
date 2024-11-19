from Adafruit_Thermal import *
import time
printer = Adafruit_Thermal('COM5', 9600, timeout=5)

# Test inverse on & off
printer.inverseOn()
printer.println("Inverse ON")
printer.inverseOff()
printer.justify('C')
printer.println("SAMPLE")
printer.println("SAMPLE")
printer.println("SAMPLE")
printer.println("SAMPLE")