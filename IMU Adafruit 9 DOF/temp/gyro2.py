#!/usr/bin/python
 
from L3GD20 import L3GD20
from LMS303DS import LMS303DS 
import numpy as np
from madgwickahrs import MadgwickAHRS
import time
import math
 
# Communication object
s = L3GD20(busId = 0, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
ss = LMS303DS(busId = 0, slaveAddr = 0x1e, ifLog = False, ifWriteBlock=False)
# Configuration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("250dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)
s.Init() # Do measurements after Init!
s.Calibrate()
print "hello gyro"

def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_z_rotation(x,y,z):
    radians = math.atan2(z, dist(x,y))
    return math.degrees(radians)

def calibrateall(s, ss):
    cnt = 0;
    time_diff = 0.01
    gyro_x_cal =0
    gyro_y_cal =0
    gyro_z_cal =0
    for i in range(0, int(3.0 / time_diff)):
        time.sleep(time_diff - 0.005) 
        (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z) = s.Get_CalOut_Value()
        gyro_x_cal += gyro_scaled_x;                                              #Add the gyro x offset to the gyro_x_cal variable
        gyro_y_cal += gyro_scaled_y;                                              #Add the gyro y offset to the gyro_y_cal variable
        gyro_z_cal += gyro_scaled_z;                                              #Add the gyro z offset to the gyro_z_cal variable
        cnt=cnt+1
    gyro_x_cal /= cnt
    gyro_y_cal /= cnt
    gyro_z_cal /= cnt
    return  (gyro_x_cal, gyro_y_cal, gyro_z_cal)   

   # return (gyro_scaled_x,gyro_scaled_y,gyro_scaled_z,accel_scaled_x,accel_scaled_y, accel_scaled_z)
def calibrate(s, ss):
#    print "hello"

    (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z) = s.Get_CalOut_Value()
    (accel_scaled_x, accel_scaled_y, accel_scaled_z) = ss.getAccel()


    last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

    gyro_offset_x = gyro_scaled_x 
    gyro_offset_y = gyro_scaled_y

    gyro_total_x = (last_x) - gyro_offset_x
    gyro_total_y = (last_y) - gyro_offset_y
    return gyro_total_x, gyro_total_y, gyro_offset_x, gyro_offset_y, last_x, last_y 



if __name__ == "__main__":
    new_data =  MadgwickAHRS()
    while 1:
        
        gyr = np.array(s.Get_CalOut_Value())
        acc = np.array(ss.getAccel())
        print(gyr)
#        while not bool(sm.isMagReady()):
#            print "not ready"
#            time.sleep(0.1)
#        mag = np.array(sm.getMag())
        gyr_rad = gyr * (np.pi/180)
        new_data.update_imu(gyr_rad,acc)
        ahrs = new_data.quaternion.to_euler_angles()
#        print ahrs
        time.sleep(1)
