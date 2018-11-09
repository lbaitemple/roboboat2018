from PWM import T200

a=T200(0x70, 50)


while True:
    a.setServo(0, 10)
    time.sleep(1)

