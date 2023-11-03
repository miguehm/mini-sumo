from machine import Pin
import time

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
    input("enter to run")
    while True:
        """
        move_forward()
        print("Forward")
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(2)
        move_backward()
        print("Backward")   
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(2)
        
        turn_right()
        print("Forward")
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(2)
        turn_left()
        print("Backward")   
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(2)
        """
        
        rotate_right()
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(2)
        rotate_left()
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(2)
