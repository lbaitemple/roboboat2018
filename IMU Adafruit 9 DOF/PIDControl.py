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
lsm303 = Adafruit_Sensor.LSM303()
l3gd20 = Adafruit_Sensor.L3GD20()
# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

##########################################################
import array
import numpy
initalPost = 0
yawArray = [ 0, 0, 0, 0, 0 ]
############################################################


print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:


   for i in range (0,5):
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    gyro = l3gd20.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    gyro_x, gyro_y, gyro_z = gyro
    gyro_x=gyro_x/57.3
    gyro_y=gyro_y/57.3
    gyro_z=gyro_z/57.3
#    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5} Gyro X={6}, Gyro Y={7}, Gyro Z={8}'. format(
#          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z, gyro_x, gyro_y, gyro_z))

    pitch = math.atan2 (accel_y ,( math.sqrt ((accel_x * accel_x) + (accel_z * accel_z))));
    roll = math.atan2(-accel_x ,( math.sqrt((accel_y * accel_y) + (accel_z * accel_z))));
    Yh = (mag_y * math.cos(roll)) - (mag_z * math.sin(roll));
    Xh = (mag_x * math.cos(pitch))+(mag_y * math.sin(roll)*math.sin(pitch)) + (mag_z * math.cos(roll) * math.sin(pitch));
    yaw =  math.atan2(Yh, Xh);
    roll = roll*57.3;
    pitch = pitch*57.3;
    yaw = yaw*57.3;
#    print pitch, roll, yaw
    # Wait half a second and repeat.
    time.sleep(0.5)


   
    yawArray[i] = int(yaw)
    print "adding to the array", yawArray, i
    print "The mean is ", int(numpy.mean(yawArray))
    yaw = int(numpy.mean(yawArray))

#########################################################################################
# we should creating insert an array and take the average of the array after X inputs and reset the array once we print out where the IMU is positioned

# Interger values will make caluclations easier for angle change calculations.
       
    Straight = int(yaw) - initalPost 
    if initalPost == 0:
	print "Waiting for more data..."
    elif int(yaw) < initalPost:
	print "turning right"
    elif int(yaw) > initalPost:
	print "turning left"
    elif Straight == 0:
	print "Moving Straight"
    initalPost = int(yaw)
    print "Current location", initalPost
   
