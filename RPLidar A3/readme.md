## Progress report 2/11/19
Working ROS package for lidar sensor with ROS RVIZ on Jetson TX2 with USB
Goals
- Get it to work with Raspberry Pi 3B using UART
## Progress report 2/14/19
- Downloaded the git package from slammtec and catkin_make all the files
- Ran into issues where USB permissions needed to be allowed for the RPLidar (fixed)
- Ran into RPLidar error -1 used https://github.com/Slamtec/rplidar_ros/issues/1 to fix issue where we had to change the node.cpp 
```
//angle_compensate_multiple = (int)(1000*1000/current_scan_mode.us_per_sample/10.0/360.0);
angle_compensate_multiple = 1;
```
## Run the program using...

to run the program open a terminal and run
```
roscore
```
then go into the workspace and run the following
```
source devel/setup.bash
roslaunch rplidar_ros view_rplidar_a3.launch
```
Then RVIZ should work
- * This following was running on a Raspberry Pi 3B and ROS kinetic 
