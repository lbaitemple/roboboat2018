Install Jetpack 3.2.1 on Ubuntu 16.04

```
bash ./JetPack-L4T-3.1-linux-x64.run

```
![alt test](https://github.com/lbaitemple/roboboat2018/blob/master/TX2/test1.png)

# Boot From SD card

1. Before you consider booting from the SD card make sure that everything on the internal memory works first.
2. Once the internal memory kenerl is built you are ready to copy everything over to the SD card.

## SD card 
For this project we will be using most of the Jetsonhacks tutorial link here : https://www.youtube.com/watch?v=kVwG-Blz0zQ
1. Format the SD card make sure it is ext4

```
sudo cp -ax / (drag file here)
```
# roboboat2018
 
# Flashing Jetson TX2 Board

check reference at:

https://github.com/NVIDIA-Jetson/jetson-trashformers/wiki/Jetson%E2%84%A2-Flashing-and-Setup-Guide-for-a-Connect-Tech-Carrier-Board

- Download and install for Nvidia Jetson TX2(LT4 28.2.1) 
1. Jetpack 3.2.1 compatible with ZED Stereo Camera 2.6 with Cuda 9.0
2. No action (Visionwork) yet

- To place the system in Force USB Recoverymode

3. Press and Hold the recovery (RUC), while releasing the RUC, press reset (RST)
4. Wait 2 seconds and release the RUC button

- The actual code:
```
    $sudo ./flash.sh jetson-tx2 mmcblk0p1
   
``` 
# Make Kernel

(new kernel update link) https://github.com/jetsonhacks/buildJetsonTX2Kernel

- Watch: https://www.youtube.com/watch?v=80c5j0rSN_0
``` 

  $sudo nvpmodel -m 0 //to check if its in Max mode
``` 

``` 
  $sudo nvpmodel -q //to verify max mode
``` 

1. Get the repository
``` 
    $cd buildJetsonTx2kernel
``` 
This srcipt will grab all the sources from the nvidia website and store them into your source file where your kernel is
``` 
    $./getkernelsources.sh
``` 
2. In local, name the new kernel (make sure to hit enter or the generic name will be used)
3. Find and select CH341, CP210x (USB ports) ( make sure they have * and not just checked)
``` 
    $./makekernel.sh
``` 
once you make the kernel you can go into your modules and delete the generic kernel as seen in the video.
```
    $./copyImage.sh //copy the image over
``` 
reboot your system and make sure the board boots using your customized kernel.
```
    $sudo reboot
``` 
# Install ROS
- https://github.com/jetsonhacks/installROSTX2
- https://shiroku.net/robotics/setup-ros-on-jetson-tx2/
``` 
cd installROSTX2
``` 
Run the install ROS TX2 
``` 
$ ./installROS.sh -p ros-kinetic-desktop -p ros-kinetic-rgbd-launch
``` 
Now that ROS is installed we need to create a workspace we can do...
``` 
$ ./setupCatkinWorkspace.sh
$ cd ~/catkin_ws/
$ source /opt/ros/kinetic/setup.bash
``` 
