"""
PyCon 2022 Circuit Playground Bluefruit Demo Hack by objectfox

A simple button reflex game using the circuit python bluefruit board.
Try to press the corresponding button when the light on each side reaches the 'top',
if you're holding it by the USB connector.
"""
import time
import random
import board
import keypad
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1  # Set the pixel brightness to 30%.

# Set up the buttons using the keypad module.
buttons = keypad.Keys((board.BUTTON_A, board.BUTTON_B), value_when_pressed=True, pull=True, max_events=1)

# Play a random wav file from the list on startup.
startup_sound = ("audio/ring.wav", "audio/space.wav", "audio/think.wav")
cp.play_file(startup_sound[2])

def current_milli_time():
    return round(time.monotonic() * 1000)

speedup = 0
next_change = current_milli_time() + 250
current_place = [random.randint(0,4), 5+random.randint(0,4)]


while True:
    button_event = buttons.events.get()  # Set up to get the button press and release events.
    if button_event:  # If there is a button event, continue onto the following code.
        if button_event.pressed:
            if button_event.pressed and button_event.key_number == 1:  # When button B is pressed...
                print("pressed b")
                if current_place[1] == 5:
                    cp.play_file(startup_sound[1])
                    speedup += 20
                    next_change = current_milli_time() + 250
                else:
                    for pixel in range(5,10):
                        cp.pixels[pixel] = (255, 0, 0)
                    cp.play_file(startup_sound[0])
                    next_change = current_milli_time() + 250
                    for pixel in range(5,10):
                        cp.pixels[pixel] = (0, 0, 0)
                    current_place[1] = random.randint(0,2)

            else:  # Otherwise...
                if current_place[0] == 4:
                    cp.play_file(startup_sound[1])
                    speedup += 20
                    next_change = current_milli_time() + 250
                else:
                    for pixel in range(0,5):
                        cp.pixels[pixel] = (255, 0, 0)
                    cp.play_file(startup_sound[0])
                    next_change = current_milli_time() + 250
                    for pixel in range(0,5):
                        cp.pixels[pixel] = (0, 0, 0)
                    current_place[0] = random.randint(0,2)
                print("pressed a")


    if current_milli_time() > next_change:
        next_change = current_milli_time() + 250 - speedup

        cp.pixels[current_place[0]] = (0, 0, 0)  # This clears the last pixel.
        cp.pixels[current_place[1]] = (0, 0, 0)  # This clears the last pixel.

        # Move the light to the next place
        current_place[0] += 1

        if current_place[0] > 4:
            current_place[0] = 0
        
        current_place[1] -= 1

        if current_place[1] < 5:
            current_place[1] = 9
        
        cp.pixels[current_place[0]] = (0, 255, 255)  # This sets the next pixel to cyan.
        cp.pixels[current_place[1]] = (0, 255, 255)  # This sets the next pixel to cyan.

# TODO: Trigger a rainbow on X successful hits as a win state
# TODO: Figure out how to reset the game with a sustained double button press
