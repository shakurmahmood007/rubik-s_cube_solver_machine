import RPi.GPIO as GPIO
from time import sleep
# for Raspberry pi

CW = 0     # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation
SPR = 50  # Steps per Revolution (360 / 1.8)

# Defining pin numbers

DIR_L = 23
STEP_L = 24
MODE_L_MOTOR = (14, 15, 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_L, GPIO.OUT)
GPIO.setup(STEP_L, GPIO.OUT)
GPIO.output(DIR_L, CW)
GPIO.setup(MODE_L_MOTOR, GPIO.OUT)
GPIO.output(MODE_L_MOTOR, (0, 0, 0))

step_count = SPR
delay = .001

x=0
for x in range (step_count) :
    GPIO.output(STEP_L, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP_L, GPIO.LOW)
    sleep(delay)
GPIO.cleanup()