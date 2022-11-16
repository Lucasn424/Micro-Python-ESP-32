

import time

import random


from machine import Timer
from machine import Pin, PWM
from oled import OLED
from rotary_irq_esp import RotaryIRQ


oled = OLED()
oled.poweron()
oled.init_display()



r = RotaryIRQ(pin_num_clk=23,
                pin_num_dt=19,
                min_val=0,
                max_val=100,
                reverse=True,
                range_mode=RotaryIRQ.RANGE_BOUNDED)



SW=Pin(22, Pin.IN)

val=SW.value()
oled.draw_text(0,0,'{:4d}'.format(val))
oled.display()














'''
import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)
'''
