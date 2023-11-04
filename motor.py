from machine import Pin
from time import sleep

# Defining motor pins

#OUT1  and OUT2
In1=Pin(10,Pin.OUT) 
In2=Pin(11,Pin.OUT)  

#OUT3  and OUT4
In3=Pin(12,Pin.OUT)  
In4=Pin(13,Pin.OUT)  

def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
def move_backward():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    
def turn_right():
    In1.low()
    In2.low()
    In3.low()
    In4.high()
    
def turn_left():
    In1.low()
    In2.high()
    In3.low()
    In4.low()
    
def rotate_left():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    
def rotate_right():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
   
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    
if __name__ == "__main__":
    functions = [move_forward, move_backward, turn_right, turn_left, rotate_left, rotate_right]
    
    print("running")
    sleep(1.5)
    
    sleep_time = 2
    while True:
        for function in functions:
            print(function.__name__)
            function()
            sleep(sleep_time)
            print("Stop")
            stop()
            sleep(sleep_time)
