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
    rospy.loginfo("I heard %f %f", msg.x, msg.y)
    print msg.x
    a.setServo(0, msg.x)
  
    
    
'''
    if msg.data == 1:
	random_callback1(msg)
    if msg.data == 2:
	random_callback2(msg)
    if msg.data == 3:
	random_callback3(msg)
'''
def startmotor():
	rospy.init_node('motorcontrol')
#       sub=rospy.Subscriber('motor/speed', Int32, random_callback,queue_size=1)
        sub=rospy.Subscriber('motor/speed', Vector3, random_callback,queue_size=1)
        print "Im gonna go again"
        rospy.spin()

if __name__=='__main__':
#This is a top level function that handles motor controls in ROS
        startmotor()
	

''' 
Functions below can be utilized for settings

def random_callback1(msg):
	    global counter
	    global check
	    global preVal
       	    rospy.loginfo("I heard ONNE %s", msg.data)
	    print "Count is,", counter
	    print "Check is,", check 
	    if counter > 0:
		if msg.data != preVal:
		    check = 1	
	        else: 
		    check = 0
            a.setServo(0, msg.data)
	    print "In callback"
	    counter = counter + 1
	    preVal = msg.data

def random_callback2(msg):
	    global counter
	    global check
	    global preVal
       	    rospy.loginfo("I heard TWO %s", msg.data)
	    print "Count is,", counter
	    print "Check is,", check 
	    if counter > 0:
		if msg.data != preVal:
		    check = 1	
	        else: 
		    check = 0
            a.setServo(0, msg.data)
	    print "In callback"
	    counter = counter + 1
	    preVal = msg.data

def random_callback3(msg):
	    global counter
	    global check
	    global preVal
       	    rospy.loginfo("I heard THREE %s", msg.data)
	    print "Count is,", counter
	    print "Check is,", check 
	    if counter > 0:
		if msg.data != preVal:
		    check = 1	
	        else: 
		    check = 0
            a.setServo(0, msg.data)
	    print "In callback"
	    counter = counter + 1
	    preVal = msg.data
'''

