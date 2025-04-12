from machine import Pin,PWM
import time

MID = 1500000
MIN = 1000000
MAX = 2000000

led = Pin(25,Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(50)
pwm.duty_ns(MID)

while True:
    pwm.duty_ns(MIN)
    led.on()
    time.sleep(1)
    pwm.duty_ns(MID)
    led.off()
    time.sleep(1)
    pwm.duty_ns(MAX)
    led.on()
    time.sleep(1)
    
#https://www.instructables.com/Servo-Motor-Control-Using-Raspberry-Pi-Pico/