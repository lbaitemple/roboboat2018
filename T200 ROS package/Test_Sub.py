# Using this template from 
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#!/usr/bin/env python
    import rospy
    from std_msgs.msg import String
    from sensor_msgs.msg import Image
 #   from Servo_Example.py import setServo HELP US


    def Dosomething(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.height)
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.width)
    pixels = data.data
    
        
    def listener():
    
       # In ROS, nodes are uniquely named. If two nodes with the same
       # node are launched, the previous one is kicked off. The
       # anonymous=True flag means that rospy will choose a unique
       # name for our 'listener' node so that multiple listeners can
       # run simultaneously.
       rospy.init_node('Motor', anonymous=True)
   
       rospy.Subscriber("/zed/right/image_rect_color
", Image, Dosomething)
   
       # spin() simply keeps python from exiting until this node is stopped
       rospy.spin()
   
   if __name__ == '__main__':
       listener()
