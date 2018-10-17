# roboboat2018

check reference at

https://github.com/NVIDIA-Jetson/jetson-trashformers/wiki/Jetson%E2%84%A2-Flashing-and-Setup-Guide-for-a-Connect-Tech-Carrier-Board

(new kernel update link) https://github.com/jetsonhacks/buildJetsonTX2Kernel

 https://github.com/jetsonhacks/installROSTX2
 
# Kernel installation

```
git clone https:https://github.com/jetsonhacks/buildJetsonTX2Kernel.git
```
```
cd buildJetsonTX2Kernel
```
get the sources for the kernel and edit the config
```
./getKernelSources.sh
```
next save the file and run next command
```
./makeKernel.sh
```
copy the image over
```
./copyImage.sh
```
restart the computer 
```
sudo reboot
```
after you restart the computer check to makre the kernel copied correctly
Also remove delete the folders as mentioned in the video expect do not delete kernel folder in usr/src
https://www.youtube.com/watch?v=80c5j0rSN_0

# Install the ROS- Kinetic

I followed the 
https://shiroku.net/robotics/setup-ros-on-jetson-tx2/
and 
https://www.jetsonhacks.com/2017/03/27/robot-operating-system-ros-nvidia-jetson-tx2/




```
git clone git clone https://github.com/jetsonhacks/installROSTX2.git
```
```
cd installROSTX2
```
```
./installROSTX2
or  
./installROS.sh -p ros-kinetic-desktop -p ros-kinetic-rgbd-launch
```

```
./setupCatkinWorkspace.sh Roboboatv0.1
```
after creating a workspace you still have to do the following...
```
cd ~/Roboboatv0.1/
source /opt/ros/kinetic/setup.bash
```

if you are having running rosrun run and try again
this command will run shell as the target user
```
sudo -s
```
