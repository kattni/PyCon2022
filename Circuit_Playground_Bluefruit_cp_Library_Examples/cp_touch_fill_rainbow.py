"""This example uses the capacitive touchpads on the CPB. They are located around the outer edge
of the board and are labeled A1-A6 and TX. (Audio is not a touchpad.) This example lights up all the
NeoPixels a different color of the rainbow for each pad touched!"""
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
    if cp.touch_A1:
        print("Touched A1!")
        cp.pixels.fill((255, 0, 0))
    if cp.touch_A2:
        print("Touched A2!")
        cp.pixels.fill((210, 45, 0))
    if cp.touch_A3:
        print("Touched A3!")
        cp.pixels.fill((155, 100, 0))
    if cp.touch_A4:
        print("Touched A4!")
        cp.pixels.fill((0, 255, 0))
    if cp.touch_A5:
        print("Touched A5!")
        cp.pixels.fill((0, 135, 125))
    if cp.touch_A6:
        print("Touched A6!")
        cp.pixels.fill((0, 0, 255))
    if cp.touch_TX:
        print("Touched TX!")
        cp.pixels.fill((100, 0, 155))
    time.sleep(0.1)
