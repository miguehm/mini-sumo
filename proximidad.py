from machine import Pin
from time import sleep, sleep_us, ticks_us

trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Has no time sleep
def get_distance():
    trig.value(0)
    sleep(0.1)
    trig.value(1)
    #sleep_us(2) # is necesary?
    trig.value(0)
    while echo.value()==0:
      pulse_start = ticks_us()
    while echo.value()==1:
      pulse_end = ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165 / 1000000
    distance = round(distance, 0)
    print ('Distance:',"{:.0f}".format(distance),'cm')
    return distance

def testing():
    while True:
        trig.value(0)
        time.sleep(0.1)
        trig.value(1)
        # sleep_us(2)
        trig.value(0)
        while echo.value()==0:
          pulse_start = time.ticks_us()
        while echo.value()==1:
          pulse_end = time.ticks_us()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17165 / 1000000
        distance = round(distance, 0)
        print (f'Distance: {distance:.0f} cm')
        #sleep(1)

if __name__ == "__main__":
    while True:
        get_distance()
        sleep(1/100)
