# T200 Motor Control 
This is a ROS package setting the T200 Thrusters from Blue Robotics a subcriber.
- We are using the PWM chart provided by BlueRobotics to set the correct PWMs for Foward,Backwards, and stop.
- For the PWM signal we are using the PCA9685 16 channel chip using i2c interfacing with a Jetson TX2 board.
#How to publish to motors using ROSTOPIC PUB...

```
rostopic pub motor/speed geometry_msgs/Vector3 '{x: 100,y: 100,  z: 1}'
```
