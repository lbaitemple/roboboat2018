# Import the LSM303 module.
import Adafruit_Sensor
import math
# Create a LSM303 instance.
lsm303 = Adafruit_Sensor.LSM303()
l3gd20 = Adafruit_Sensor.L3GD20()


class Sensor(object):

    def read(self):
        accel, mag = lsm303.read()
        gyro = l3gd20.read()
        accel_x, accel_y, accel_z = accel
        mag_x, mag_y, mag_z = mag
        gyro_x, gyro_y, gyro_z = gyro
        gyro_x=gyro_x/57.3
        gyro_y=gyro_y/57.3
        gyro_z=gyro_z/57.3
        pitch = math.atan2 (accel_y ,( math.sqrt ((accel_x * accel_x) + (accel_z * accel_z
))));
        roll = math.atan2(-accel_x ,( math.sqrt((accel_y * accel_y) + (accel_z * accel_z))
));
        Yh = (mag_y * math.cos(roll)) - (mag_z * math.sin(roll));
        Xh = (mag_x * math.cos(pitch))+(mag_y * math.sin(roll)*math.sin(pitch)) + (mag_z *
 math.cos(roll) * math.sin(pitch));
        yaw =  math.atan2(Yh, Xh);
        roll = roll*57.3;
        pitch = pitch*57.3;
        yaw = yaw*57.3;

        return pitch, roll, yaw
