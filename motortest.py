from machine import Pin
from time import sleep

out1FL = PWM(0)
out2FL = PWM(1)
out1FL.freq(5000)
out2FL.freq(5000)


# init
out1FL.duty_u16(0)
out2FL.duty_u16(0)

while True:
    # Forward
    out1FL.duty_u16(64000)
    sleep(1)
    # Half speed
    out1FL.duty_u16(32000)
    sleep(1)
    # Backward
    out1FL.duty_u16(0)
    sleep(0.1)
    out2FL.duty_u16(64000)
    sleep(1)
    # Half speed
    out2FL.duty_u16(32000)
    sleep(1)
    out2FL.duty_u16(0)
    sleep(0.01)
