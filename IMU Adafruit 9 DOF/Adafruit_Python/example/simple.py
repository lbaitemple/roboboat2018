# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the LSM303 module.
#import Adafruit_LSM303
import Adafruit_Sensor
import math
# Create a LSM303 instance.
sensor = Adafruit_Sensor.Sensor()

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    pitch, roll, yaw = sensor.read()
    print pitch, roll, yaw
    # Wait half a second and repeat.
    time.sleep(0.5)
