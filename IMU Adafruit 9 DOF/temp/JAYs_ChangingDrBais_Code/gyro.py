#!/usr/bin/python
 
from L3GD20 import L3GD20
from LMS303DS import LMS303DS
import time
import math
 
# Communication object
s = L3GD20(busId = 0, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
ss = LMS303DS(busId = 0, slaveAddr = 0x1e, ifLog = False, ifWriteBlock=False)
angle_pitch =0
angle_roll=0
angle_yaw=0
set_gyro_angles=1
angle_pitch_output=0
angle_roll_output=0
angle_yaw_output=0
 
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
#    print "hello gyro"
    (accel_scaled_x, accel_scaled_y, accel_scaled_z) = ss.getAccel()
#    print "hello acce"
    last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

    gyro_offset_x = gyro_scaled_x 
    gyro_offset_y = gyro_scaled_y

    gyro_total_x = (last_x) - gyro_offset_x
    gyro_total_y = (last_y) - gyro_offset_y
    return gyro_total_x, gyro_total_y, gyro_offset_x, gyro_offset_y, last_x, last_y 


def get_rotation(s, ss, gyro_x_cal, gyro_y_cal, gyro_z_cal):   
    global angle_pitch, angle_roll, angle_yaw, set_gyro_angles, angle_pitch_output, angle_roll_output
    (gyro_x, gyro_y, gyro_z) = s.Get_CalOut_Value()
    (acc_x, acc_y, acc_z)=  ss.getAccel()
    gyro_x -= gyro_x_cal;                                                
    gyro_y -= gyro_y_cal;                                                
    gyro_z -= gyro_z_cal;                                                
         
    #Gyro angle calculations . Note 0.0000611 = 1 / (250Hz x 65.5)
    angle_pitch += gyro_x * 0.0000611;                                   #Calculate the traveled pitch angle and add this to the angle_pitch variable
    angle_roll += gyro_y * 0.0000611;     
    angle_yaw += gyro_z * 0.0000611;                                #Calculate the traveled roll angle and add this to the angle_roll variable
  #0.000001066 = 0.0000611 * (3.142(PI) / 180degr) The Arduino sin function is in radians
    angle_pitch += angle_roll * math.sin(gyro_z * 0.000001066);               #If the IMU has yawed transfer the roll angle to the pitch angel
    angle_roll -= angle_pitch * math.sin(gyro_z * 0.000001066);               #If the IMU has yawed transfer the pitch angle to the roll angel
    angle_yaw -= angle_yaw * math.sin(gyro_z * 0.000001066);               #If   
  #Accelerometer angle calculations
    acc_total_vector = math.sqrt((acc_x*acc_x)+(acc_y*acc_y)+(acc_z*acc_z));  #Calculate the total accelerometer vector
  #57.296 = 1 / (3.142 / 180) The Arduino asin function is in radians
    angle_pitch_acc = math.asin(acc_y/acc_total_vector)* 57.296;       #Calculate the pitch angle
    angle_roll_acc = math.asin(acc_x/acc_total_vector)* -57.296;       #Calculate the roll angle
  
    angle_pitch_acc -= 0.0;                                              #Accelerometer calibration value for pitch
    angle_roll_acc -= 0.0;                                               #Accelerometer calibration value for roll

    if(set_gyro_angles):                                                 #If the IMU is already started
        angle_pitch = angle_pitch * 0.9996 + angle_pitch_acc * 0.0004;     #Correct the drift of the gyro pitch angle with the accelerometer pitch angle
        angle_roll = angle_roll * 0.9996 + angle_roll_acc * 0.0004;        #Correct the drift of the gyro roll angle with the accelerometer roll angle
    else:                                                                #At first start
        angle_pitch = angle_pitch_acc;                                     #Set the gyro pitch angle equal to the accelerometer pitch angle 
        angle_roll = angle_roll_acc;                                       #Set the gyro roll angle equal to the accelerometer roll angle 
        set_gyro_angles = true;                                            #Set the IMU started flag
    
  
    #To dampen the pitch and roll angles a complementary filter is used
    angle_pitch_output = angle_pitch_output * 0.9 + angle_pitch * 0.1;   #Take 90% of the output pitch value and add 10% of the raw pitch value
    angle_roll_output = angle_roll_output * 0.9 + angle_roll * 0.1;      #Take 90% of the output roll value and add 10% of the raw roll value
    return (angle_pitch_output,angle_roll_output)

def getfilter_rotation(s, ss,gyro_total_x, gyro_total_y, gyro_offset_x, gyro_offset_y , last_x, last_y):
    K = 0.98
    K1 = 1 - K
    time_diff = 0.01

    for i in range(0, int(3.0 / time_diff)):
        time.sleep(time_diff - 0.005) 
 #       print "hello"
        (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z) = s.Get_CalOut_Value()
        (accel_scaled_x, accel_scaled_y, accel_scaled_z) = ss.getAccel()
    
        gyro_scaled_x -= gyro_offset_x
        gyro_scaled_y -= gyro_offset_y
    
        gyro_x_delta = (gyro_scaled_x * time_diff)
        gyro_y_delta = (gyro_scaled_y * time_diff)

        gyro_total_x += gyro_x_delta
        gyro_total_y += gyro_y_delta

        rotation_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
        rotation_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

        last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
        last_y = K * (last_y + gyro_y_delta) + (K1 * rotation_y)
    
      #  print "{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f}".format( time.time() - now, (rotation_x), (gyro_total_x), (last_x), (rotation_y), (gyro_total_y), (last_y))
   # print "{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f}".format( time.time() - now, (last_x), gyro_total_x, (last_x), (last_y), gyro_total_y, (last_y))
   # print "after ",last_x, last_y, rotation_x, rotation_y
    return (last_x, last_y)


(gyro_x_cal, gyro_y_cal, gyro_z_cal)   =calibrateall(s,ss)
print (gyro_x_cal, gyro_y_cal, gyro_z_cal)   
get_rotation(s,ss,gyro_x_cal, gyro_y_cal, gyro_z_cal)
while 1==1:
    
    (rx,ry)=get_rotation(s,ss,gyro_x_cal, gyro_y_cal, gyro_z_cal)
    print (rx, ry)
    time.sleep(1)
