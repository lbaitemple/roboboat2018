#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x70)
pwm.setPWMFreq(60)  # Set frequency to 60 Hz

# pulseVal approximations for ESC
# ~170 = stopped
#  140-170 = counter clockwise (foward)
#  170-190 = clockwise	(backwards)

settings = 3; # Setting value determines direction of motor

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


