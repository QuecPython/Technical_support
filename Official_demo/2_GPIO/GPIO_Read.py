"""
Please refer to the Chinese information:https://python.quectel.com/doc/API_reference/zh/
Please refer to English information:    https://python.quectel.com/doc/doc/API_reference/en/
"""
"""
This code sets up a list of three GPIO objects (connected to pins 11, 12, and 13) with input mode and internal pull-down resistance. It then continuously loops through the list and prints out the current level of each GPIO object. Finally, it delays for 300ms before repeating the loop.

The Pin function is called to create each GPIO object, with the following parameters:

Pin.GPIO11, Pin.GPIO12, Pin.GPIO13 - Specifies the pin number for each GPIO object.
Pin.IN - Sets the GPIO object to input mode.
Pin.PULL_PD - Enables an internal pull-down resistor on the specified pin.
1 - Specifies that the initial value of the pin is high, but input mode this parameter is invalid and can be ignored.
In the main loop, the IOlist is iterated over using a for loop, and the print() function is used to display the state of each GPIO object, along with its pin number and current level. The utime.sleep_ms() function is called to create a delay of 300ms after each loop iteration.
"""

from machine import Pin
import utime

# Set up a list of GPIO objects with input mode and pull-down resistance
IOlist = []
IOlist.append(Pin(Pin.GPIO11, Pin.IN, Pin.PULL_PD , 1))
IOlist.append(Pin(Pin.GPIO12, Pin.IN, Pin.PULL_PD , 1))
IOlist.append(Pin(Pin.GPIO13, Pin.IN, Pin.PULL_PD , 1))

while True:
    # Loop through the list of GPIO objects and print out their current level
    for x in range(int(len(IOlist))):
        print(IOlist[x], 'GPIO{} level'.format(x + 1), end='  : ')
        print(IOlist[x].read())
    # Delay for 300ms before looping again
    utime.sleep_ms(300)

