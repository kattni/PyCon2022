"""THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the simpleio.mpy library.

This example uses the light sensor on the CP, located net to the picture of the eye on the board.
Once you have the library loaded, try shining a flashlight on your CP to watch the number of
NeoPixels lit up increase, or try covering up the light sensor to watch the number decrease."""
import time
from adafruit_circuitplayground import cp
import simpleio

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

while True:
    # light value remapped to pixel position
    peak = simpleio.map_range(cp.light, 0, 320, 0, 10)
    print(cp.light)
    print(int(peak))

    for i in range(0, 10, 1):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)
