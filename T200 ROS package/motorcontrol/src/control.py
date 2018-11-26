#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from geometry_msgs.msg import Vector3
from random import randint
from PWM import T200

a=T200(0x70, 50)
counter = 0
check = 0
preVal = 0

def random_callback(msg):
    rospy.loginfo("Your X value %f %f", msg.x, msg.y)
    print "Your X value is ", msg.x 
    print "Your Y value is ", msg.y 
    print "Your Z value is ", msg.z 
    a.setServo(0, msg.x, msg.y)
  
    
    

def startmotor():
	rospy.init_node('motorcontrol')
#       sub=rospy.Subscriber('motor/speed', Int32, random_callback,queue_size=1)
        sub=rospy.Subscriber('motor/speed', Vector3, random_callback,queue_size=1)
        print "Im gonna go again"
        rospy.spin()

if __name__=='__main__':
#This is a top level function that handles motor controls in ROS
        startmotor()

