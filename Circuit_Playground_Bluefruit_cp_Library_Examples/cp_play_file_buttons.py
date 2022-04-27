"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2022 REPO!
Copy the "ring.wav" and "think.wav" files to your CIRCUITPY drive.

Once the files are copied, this example plays a different wav file for each button pressed!"""
from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.play_file("ring.wav")
    if cp.button_b:
        cp.play_file("think.wav")
