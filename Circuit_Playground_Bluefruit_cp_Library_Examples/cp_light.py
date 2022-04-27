"""This example uses the light sensor on your CP, located next to the picture of the eye. Try
shining a flashlight on your CP, or covering the light sensor with your finger to see the values
increase and decrease."""
import time
from adafruit_circuitplayground import cp

while True:
    print("Light:", cp.light)
    time.sleep(1)
