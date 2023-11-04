from machine import Pin, ADC
from time import sleep

digital_pin = Pin(18, Pin.IN)
#analog_pin = ADC(Pin(26))
#analog_pin.atten(ADC.ATTN_11DB)

def get_color():
    return digital_pin.value()

if __name__ == "__main__":
    while True:
        print(f'{"black" if get_color() else "white"}')
        #print(f'{analog_pin.read_u16()}')
        sleep(1/100)
