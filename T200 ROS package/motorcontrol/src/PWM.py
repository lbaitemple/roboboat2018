#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time


class T200:
    def __init__(self, port=0x70, freq=60):
        self.port = port
        self.freq = freq
        self.pwm = PWM(self.port)
        self.pwm.setPWMFreq(self.freq)

    def setServo(self, channel, value):
	while (value < 12):
		number = 10
        	number = float(number)
       		number = number / 100 * 450
        	number = number + value
        	number = int(number);
        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel, 0, number)
		time.sleep(1)	
		number = 50
		number = float(number)
        	number = number / 100 * 450
        	number = number + value
        	number = int(number);
        	print "Writing ", number, " to motor"
        	self.pwm.setPWM(channel, 0, number)
		time.sleep(1)
	
	print "I'm done"




