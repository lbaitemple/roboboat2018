# The MIT License (MIT)
#
# This package can work thanks to packages and modules written by Tony Dicola.
# This code was based on Adafruit_LSM303.py module by Tony Dicola.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import Adafruit_GPIO.I2C #Import the module I2C which belong to Adafruit_GPIO Package
import struct #Import struct module

#Gyroscope Address
#Depending on which is connected to SDO pin of the gyroscope the slave address change:
#-L3GD20_address = 0x6B <----SDO connected to power supply (my case)
#-L3GD20_address = 0x6A <----SDO conncected to GND
L3GD20_address = 0x6B
#Control Register Adresss
L3GD20_fifo_ctrl_reg = 0x2e	
L3GD20_ctrl_reg5=0x24
L3GD20_ctrl_reg4=0x23
L3GD20_ctrl_reg1=0x20
#Range Settings
L3GD20_range_200dps =0b00000000 #  +/-200dps
L3GD20_range_500dps =0b00010000 #  +/-500dps
L3GD20_range_2000dps =0b00100000 # +/- 2000dps
#Frequency Output Data Rate Setting
L3GD20_95Hz = 0b00000000
L3GD20_190Hz = 0b01000000
L3GD20_380Hz = 0b10000000
L3GD20_760Hz = 0b11000000
#CutOff Setting(The actual value of CutOff depends from the frequency setting(see L3GD20 datasheets))
L3GD20_low = 0b00000000
L3GD20_medium_low = 0b00010000
L3GD20_medium_high = 0b00100000
L3GD20_high = 0b00110000
#First register containing measurement
L3GD20_out_x_L=0x28

class L3GD20(object):
        #L3GD20 Gyroscope
        def __init__(self, **kwargs):
                #Initialing Gyroscope
                self._address = L3GD20_address
                self._gyr = Adafruit_GPIO.I2C.get_i2c_device(self._address, **kwargs) #I instantiate the object returned by get_i2c_device function which is located in Module I2C.
                #If you want to change range, change the name of variable assigned to self_range among these:
                #-L3GD20_range_200dps
                #-L3GD20_range_500dps
                #-L3GD20_range_2000dps
                self._range = L3GD20_range_200dps
                #If you want to change the output data rate, change the name of variable assigned to self.freq among these:
                #-L3GD20_95Hz
                #-L3GD20_190Hz
                #-L3GD20_380Hz
                #-L3GD20_760Hz
                self._freq = L3GD20_95Hz
                #If you want to change range, change the name of variable assigned to self_range among these:
                #-L3GD20_low
                #-L3GD20_medium_low
                #-L3GD20_medium_high
                #-L3GD20_high
                self._cutoff = L3GD20_low
                #Initialising Gyroscope
                #Setting the range
                self._gyr.write8(L3GD20_ctrl_reg4, 0b00000000 + self._range)
                #Enabling FIFO Area
                self._gyr.write8(L3GD20_ctrl_reg5,0b01000000)
                #Enabling gyroscope, axis and setting frequency and cut-off
                self._gyr.write8(L3GD20_ctrl_reg1, self._cutoff + self._freq + 0b00001111) #The last sequence is to power-up the gyroscope and enable axis. 
                #Set The Acquisition Mode
                self._gyr.write8(L3GD20_fifo_ctrl_reg,0b00010000)


                
        def read(self):
                #Read the gyroscope value. A tuple of tuples will
                #be returned with:
                #(ang_velocity X, ang_velocity Y, ang_velocity Z)
                ang_vel_raw = self._gyr.readList(L3GD20_out_x_L|0x80, 6)  ##It returns a bytes object(an instance of byte class). In this case It is a sequence of 6 bytes. The format is this: b'\x00\x00\x00\x00\x00\x00'
                ang_vel = struct.unpack('<hhh', ang_vel_raw)
                return(ang_vel)
                

