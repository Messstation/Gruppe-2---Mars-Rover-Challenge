#Track1: Ramp module
import conf
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

def start():
    init()
    while GPIO.input(conf.tasterStop) == False:
        pass
    return True

def init():
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    return True

def Texit():
    GPIO.output(18, GPIO.LOW)
    return


