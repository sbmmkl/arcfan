#thearc.in

import RPi.GPIO as GPIO

import time
import os

def measure_temp():

        temp = os.popen("vcgencmd measure_temp").readline()
        val = temp.replace("'C","")
        val = val.replace("temp=","")
        return(val)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.OUT)



red_led = GPIO.PWM(25,100)

red_led.start(0)

pause_time = 0.1

temp = 1

while True:


        val = measure_temp()
        val = val.replace(".0\n","")
        temp = int(val)
        if ( temp > 50 and temp < 54):
                for x in range (100):
                        red_led.ChangeDutyCycle(50)
                #       print("###### 1")
                        time.sleep(pause_time)

        elif (temp > 53 and temp < 60):
                for x in range (100):
                        red_led.ChangeDutyCycle(70)
                #       print("############ 2")
                        time.sleep(pause_time)

        elif (temp > 59):
                for x in range (100):
                        red_led.ChangeDutyCycle(100)
                #       print("################# 3")
                        time.sleep(pause_time)

        elif (temp <50):
                for x in range (100):
                        red_led.ChangeDutyCycle(30)
                #       print("#### 0")
                        time.sleep(pause_time)


        print(temp)

GPIO.cleanup()
