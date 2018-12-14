from L3GD20 import L3GD20
from LMS303DS import LMS303DS
import time
import math
import numpy as np
from madgwickahrs import MadgwickAHRS

#Communication Device addressing for i2c is 
#0x19 for accelerometer 
#0x1E for magnetometer
#0x6B for gyro

accel = LMS303DS(busId = 0, slaveAddr = 0x19, ifLog = False, ifWriteBlock=False)
magnet = LMS303DS(busId = 0, slaveAddr = 0x1e, ifLog = False, ifWriteBlock=False)
gyro = L3GD20(busId = 0, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

#Initalize 

angle_pitch =0
angle_roll=0
angle_yaw=0
set_gyro_angles=1
angle_pitch_output=0
angle_roll_output=0
angle_yaw_output=0

#configure
gyro.Set_PowerMode("Normal")
gyro.Set_FullScale_Value("250dps")
gyro.Set_AxisX_Enabled(True)
gyro.Set_AxisY_Enabled(True)
gyro.Set_AxisZ_Enabled(True)
gyro.Init() # Do measurements after Init!
print "hello HERE1"
gyro.Calibrate()
print "hello gyro"

#formula
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

#calibrate 
def calibrateall(gyro, accel):
    cnt = 0;
    time_diff = 0.01
    gyro_x_cal =0
    gyro_y_cal =0
    gyro_z_cal =0
    for i in range(0, int(3.0 / time_diff)):
        time.sleep(time_diff - 0.005) 
        (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z) = gyro.Get_CalOut_Value()
        gyro_x_cal += gyro_scaled_x;                                              #Add the gyro x offset to the gyro_x_cal variable
        gyro_y_cal += gyro_scaled_y;                                              #Add the gyro y offset to the gyro_y_cal variable
        gyro_z_cal += gyro_scaled_z;                                              #Add the gyro z offset to the gyro_z_cal variable
        cnt=cnt+1
    gyro_x_cal /= cnt
    gyro_y_cal /= cnt
    gyro_z_cal /= cnt
    return  (gyro_x_cal, gyro_y_cal, gyro_z_cal)   

def calibrate(gyro, accel):
    print "hello"

    (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z) = gyro.Get_CalOut_Value()
    print "hello gyro"
    (accel_scaled_x, accel_scaled_y, accel_scaled_z) = accel.getAccel()
    print "hello acce"
    last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

    gyro_offset_x = gyro_scaled_x 
    gyro_offset_y = gyro_scaled_y

    gyro_total_x = (last_x) - gyro_offset_x
    gyro_total_y = (last_y) - gyro_offset_y
    return gyro_total_x, gyro_total_y, gyro_offset_x, gyro_offset_y, last_x, last_y 

def main():
	new_data =  MadgwickAHRS()
	while 1:
        
        	gyr = np.array(gyro.Get_CalOut_Value())
        	acc = np.array(accel.getAccel())
        	while not bool(magnet.isMagReady()):
            		print "not ready"
            		time.sleep(0.1)
        	mag = np.array(magnet.getMag())
        	gyr_rad = gyr * (np.pi/180)
        	new_data.update_imu(gyr_rad,acc)
        	print(gyr, acc, mag)
        	print "---------------------------\n"
        	ahrs = new_data.quaternion.to_euler_angles()
        	print ahrs
       	 	time.sleep(1)

if __name__ == "__main__":
	main()
