import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
PIR_PIN = 22
GPIO.setup(PIR_PIN, GPIO.IN)
while True:
    i = GPIO.input(PIR_PIN)
    if i ==0:
        print("Screen off", i)
        call(["/usr/bin/vcgencmd", "display_power", "0"])
        time.sleep(1)
    elif i ==1:
        print("Screen on", i)
        call(["/usr/bin/vcgencmd", "display_power", "1"])
        time.sleep(30)


