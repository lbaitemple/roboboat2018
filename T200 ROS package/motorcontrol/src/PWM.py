#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys


class T200:
    def __init__(self, port=0x70, freq=60):
        self.port = port
        self.freq = freq
        self.pwm = PWM(self.port)
        self.pwm.setPWMFreq(self.freq)


# pulseVal approximations for ESC
# ~170 = stopped
#  140-170 = counter clockwise (foward)
#  170-190 = clockwise	(backwards)

    def setServo(self, channel, value, value2):
         	if value == 170:
			print "STOP"
		if 140 < value < 170:
			print "FOWARD"
		if 170 < value < 190:
			print "BACKWARD" 
#		print "this is channel", channel
#		print "this is value", value
		number = 10
        	number = float(number)
       		number = number / 100 * 450
		number2 = number
        	number = number + value
		number2 = number2 + value2
        	number = int(number);
		number2 = int(number2);
#        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel, 0, number)
		self.pwm.setPWM(12, 0, number2)
		time.sleep(1/4)

		number = 50
		number = float(number)
        	number = number / 100 * 450
		number2 = number
        	number = number + value
		number2 = number2 + value2
        	number = int(number);
		number2 = int(number2);
#        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel, 0, number)
		self.pwm.setPWM(12, 0, number2)
		time.sleep(1)

'''
#		print "this is channel", channel
#		print "this is value", value
		channel2 = 1;
		channel2 = int(channel2);
		number2 = 10
        	number2 = float(number2)
       		number2 = number2 / 100 * 450
        	number2 = number2 + value2
        	number2 = int(number2);
#        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel2, 0, number2)
		time.sleep(1)	

		number = 50
		number = float(number)
        	number = number / 100 * 450
        	number = number + value
        	number = int(number);
#        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel, 0, number)
		channel2 = 1;
		channel2 = int(channel2);
		number2 = 50
		number2 = float(number2)
        	number2 = number2 / 100 * 450
        	number2 = number2 + value2
        	number2 = int(number2);
#        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel2, 0, number2)
		time.sleep(1)
'''	
'''
THIS IS JAY ... I'LL be back this code down there works but we cant publish new numbers to change motor speed/direction
Will be back 1050 (@_@)
'''

'''
# Initialise the PWM device using the default address
pwm = PWM(0x70)
pwm.setPWMFreq(60)  # Set frequency to 60 Hz

# pulseVal approximations for ESC
# ~170 = stopped
#  140-170 = counter clockwise (foward)
#  170-190 = clockwise	(backwards)

settings = 1; # Setting value determines direction of motor

if settings == 1:
	pulseVal = 150  # Pulse value, backwards	
if settings == 2:
	pulseVal = 190  # Pulse value, forwards
if settings == 3:
	pulseVal = 170  # Pulse value, stopped


def setServo(channel, value):
    value = float(value)
    value = value / 100 * 450		# Duty cycle calculation
    value = value + pulseVal		# 
    value = int(value);			# Convert back to integer
    print "Writing ", value, " to motor"
    pwm.setPWM(channel, 0, value)


while (True):
     setServo(0, 10) # 0,10 orginal
     time.sleep(1)
     setServo(0, 50) # 0.50 orginal
     time.sleep(1)
'''

