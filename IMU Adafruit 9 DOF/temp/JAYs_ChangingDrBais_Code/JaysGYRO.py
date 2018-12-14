from L3GD20 import L3GD20
from LMS303DS import LMS303DS 
import numpy as np
from madgwickahrs import MadgwickAHRS
import time
import math

# Communication object
gyro = L3GD20(busId = 0, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)
accel = LMS303DS(busId = 0, slaveAddr = 0x1e, ifLog = False, ifWriteBlock=False)

if __name__ == "__main__":
	# Configuration
	s.Set_PowerMode("Normal")
	s.Set_FullScale_Value("250dps")
	s.Set_AxisX_Enabled(True)
	s.Set_AxisY_Enabled(True)
	s.Set_AxisZ_Enabled(True)
	s.Init() # Do measurements after Init!
	s.Calibrate()
	print "hello gyro"

