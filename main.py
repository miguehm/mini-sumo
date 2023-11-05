from machine import Pin, ADC
from time import sleep
from motor import move_forward, move_backward
from light import get_color
import _thread

global estado
estado = get_color()

def motor_movement():
    global estado 
    while True:
        if estado:
            move_forward()
        else:
            move_backward()
        
_thread.start_new_thread(motor_movement, ())

while True:
    estado = get_color()
    # print(f'{"black" if get_color() else "white"}')
    sleep(1/100 )