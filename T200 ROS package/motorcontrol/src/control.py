#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from random import randint

from PWM import T200

a=T200(0x70, 50)



def random_callback(msg):
    rospy.loginfo("I heard %s", msg.data)
    a.setServo(0, msg.data)

if __name__=='__main__':
	   
	rospy.init_node('motorcontrol')

   	sub=rospy.Subscriber('motor/speed', Int32, random_callback)
    	print "Im gonna go again"	
    	rospy.spin()
