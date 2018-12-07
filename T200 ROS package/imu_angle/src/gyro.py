#!/usr/bin/python
 
from L3GD20 import L3GD20
import time
import math
 
# Communication object
s = L3GD20(busId = 0, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
 
# Configuration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("250dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)
s.Init() # Do measurements after Init!
s.Calibrate()


def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

 
# Calculate angle
dt = 0.02
x = 0
y = 0
z = 0
while 1==1:
    time.sleep(dt)
    dxyz = s.Get_CalOut_Value()
    x += dxyz[0]*dt;
    y += dxyz[1]*dt;
    z += dxyz[2]*dt;
#    print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))
    print(get_x_rotation(x,y,z), get_y_rotation(x,y,z))
