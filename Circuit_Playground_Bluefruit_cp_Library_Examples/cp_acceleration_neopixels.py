"""If the switch is to the right, it will appear that nothing is happening. Move the switch to the
left to see the NeoPixels light up in colors related to the accelerometer! The CPB has an
accelerometer in the center that returns (x, y, z) acceleration values. This program uses those
values to light up the NeoPixels based on those acceleration values."""
from adafruit_circuitplayground import cp

# Main loop gets x, y and z axis acceleration, prints the values, and turns on
# red, green and blue, at levels related to the x, y and z values.
while True:
    if not cp.switch:
        # If the switch is to the right, it returns False!
        print("Slide switch off!")
        cp.pixels.fill((0, 0, 0))
        continue
    else:
        R = 0
        G = 0
        B = 0
        x, y, z = cp.acceleration
        print((x, y, z))
        if x:
            R = R + abs(int(x))
        if y:
            G = G + abs(int(y))
        if z:
            B = B + abs(int(z))
        cp.pixels.fill((R, G, B))
