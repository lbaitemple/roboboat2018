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

$sudo ./flash.sh jetson-tx2 mmcblk0p1
# Make Kernel

(new kernel update link) https://github.com/jetsonhacks/buildJetsonTX2Kernel

- Watch: https://www.youtube.com/watch?v=80c5j0rSN_0

  $sudo nvpmodel -m 0 //to check if its in Max mode

  $sudo nvpmodel -q //to verify max mode

1. Get the repository

  $cd buildJetsonTx2kernel

  $./getkernelsources.sh

2. In local, name the new kernel
3. Find and select CH341, CP210x (USB ports)

  $./makekernel.sh

  $./copyImage.sh //copy the image over

  $sudo reboot

# Install ROS
 https://github.com/jetsonhacks/installROSTX2
