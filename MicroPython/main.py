"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
from time import sleep

display.clear()
sleep(1)


display.scroll(
    "area of a rectangle is 3cm and 5cm A = 5 x 3= " + str(5 * 3)() + ("cm^2")
)
display.show(Image.happy)
sleep(0.5)


display.scroll(
    "perimeter of a rectangle is 3cm by 5cm P = 2(l+w) + 2(5+3))= "
    + str(2 * (5 * 3)) 
    + ("cm")
)
display.show(Image.happy)
sleep(0.5)
display.clear()
