# Raspberry Pi 3 spi-i2c tutorial
https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

We got the simple code to run the servo motor using Pi 3 and I2c interface

Video that worked: https://www.youtube.com/watch?v=ZEg2IjACG9s

# Jetson TX2 and I2C interface
2nd Link below is from our favorite guy : jetsonhack 
https://www.youtube.com/watch?v=qCZ_F2UgYb8
https://www.youtube.com/watch?v=wf3Vdmn4seI

I2C to control  servo motor

https://www.jetsonhacks.com/nvidia-jetson-tx2-j21-header-pinout/\

-PWM simple example C++

https://www.jetsonhacks.com/2015/10/14/pwm-servo-driver-board-nvidia-jetson-tk1/

# Week 1 (no bai)
- we were able to get PCA9685 to work with pins 27 and 28 on the JETSON tx2 which is BUS 0 on the board.
- We were able to get a basic servo motor to run to ensure that the PWM worked.
- we used the servoExample code from the JHPWMDriver from Jetson Hacks
```
	//This is currently set to give PWM to channels 0 and 12 on the board... change as you like
            pca9685->setPWM(0,0,servoMin) ;
            pca9685->setPWM(12,0,servoMin) ;
```
This website has basics that will allow us to create subcriber Motors controls example in python
https://snapcraft.io/blog/your-first-robot-introduction-to-the-robot-operating-system-2-5
