"""This example uses the capacitive touchpads around the outside of the CPB, labeled A1-A6 and TX.
(A0 is not a touch pad.) It prints to the serial console when you touch a pad. Try touching the
touch pads to see the prints!"""
import time
import board
import touchio

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)

while True:
    if touch_A1.value:
        print("Touched A1!")
    if touch_A2.value:
        print("Touched A2!")
    if touch_A3.value:
        print("Touched A3!")
    if touch_A4.value:
        print("Touched A4!")
    if touch_A5.value:
        print("Touched A5!")
    if touch_A6.value:
        print("Touched A6!")
    if touch_TX.value:
        print("Touched TX!")
    time.sleep(0.05)
