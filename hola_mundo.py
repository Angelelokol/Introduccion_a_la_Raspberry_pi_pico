from machine import Pin
import time
# led = Pin(25, Pin.OUT) # Configuración RPI Pico
led = Pin("LED", Pin.OUT) #Configuración RPI Pico W
while True:
    led.toggle()
    time.sleep_ms(500)