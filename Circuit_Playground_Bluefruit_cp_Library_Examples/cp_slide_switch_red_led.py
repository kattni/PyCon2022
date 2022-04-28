"""This example uses the slide switch to control the little red LED."""
from adafruit_circuitplayground import cp

while True:
    if cp.switch:
        cp.red_led = True
    else:
        cp.red_led = False
