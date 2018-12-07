#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from geometry_msgs.msg import Point
from random import randint
from L3GD20 import L3GD20
import time
import math

def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)



def startIMU():
	s = L3GD20(busId = 0, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
 
	# Configuration
	s.Set_PowerMode("Normal")
	s.Set_FullScale_Value("250dps")
	s.Set_AxisX_Enabled(True)
	s.Set_AxisY_Enabled(True)
	s.Set_AxisZ_Enabled(True)
	s.Init() # Do measurements after Init!
	s.Calibrate()

	rospy.init_node('imusensor')
        pub=rospy.Publisher('imu/angle', Point, queue_size=1)
        print "IMU"
        rate = rospy.Rate(10) #10 HZ
        while not rospy.is_shutdown():
             hello_str = "hello world %s" % rospy.get_time()
             rospy.loginfo(hello_str)
    	     dxyz = s.Get_CalOut_Value()
             x+=dxyz[0]/rate
	     y+=dxyz[1]/rate 
             z+=dxyz[2]/rate 
 	     cur_point = Point(get_x_rotation(x,y,z), get_y_rotation(x,y,z),0)
             pub.publish(hello_str)
             rate.sleep()

if __name__=='__main__':
#This is a top level function that handles motor controls in ROS
	startIMU()
	

