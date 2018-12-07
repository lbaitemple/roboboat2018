#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from random import randint
from PWM import T200


a=T200()
counter = 0
check = 0
preVal = 0

def random_callback(msg):
    rospy.loginfo("Your X value %f %f", msg.linear.x, msg.linear.y)
    print "Your X value is ", msg.linear.x 
    print "Your Y value is ", msg.linear.y 
    print "Your Z value is ", msg.linear.z 
    a.setServo(0, msg.linear.x, msg.linear.y)
  
    
    

def startmotor():
	rospy.init_node('motorcontrol')
        sub=rospy.Subscriber('motor/speed', Twist, random_callback,queue_size=1)
        print "Im gonna go again"
        rospy.spin()

if __name__=='__main__':
#This is a top level function that handles motor controls in ROS
        port = rospy.get_param('~i2c_port', 0x70)
        freq = rospy.get_param('~i2c_freq', 50)
	a.init(port, freq)
        startmotor()

