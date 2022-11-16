
from machine import Pin
from neopixel import NeoPixel
import time
import demo

np = NeoPixel(Pin(4), 8)


while True:
    demo.demo(np)
