"""
Please refer to the Chinese information:https://python.quectel.com/doc/API_reference/zh/
Please refer to English information:    https://python.quectel.com/doc/doc/API_reference/en/
"""
"""
This code initializes six GPIO objects (connected to pins 34, 32, 31, 1, 2, and 3), with output mode and no internal pull-up/down resistor. It then continuously loops through the list of GPIO objects twice, turning off all the GPIO objects (x.write(1)) before lighting up the next LED (y.write(0)). Finally, there's a delay of 500ms before turning on the next LED.

In the Pin function, the following parameters are used:

Pin.GPIO34, Pin.GPIO32, Pin.GPIO31, Pin.GPIO1, Pin.GPIO2, Pin.GPIO3 - Specifies the pin number for each GPIO object.
Pin.OUT - Sets the GPIO object to output mode.
Pin.PULL_DISABLE - Disables any internal pull-up/down resistor on the specified pin.
0 - Specifies the initial value of the pin as low to light up the LED.
The first for loop iterates through each GPIO object in the IOlist, and the second for loop ensures that all GPIOs are turned off before lighting up the next one with a delay of 500ms using utime.sleep_ms().
"""

from machine import Pin
import utime

# Create an empty list to hold the GPIO objects
IOlist = []

# Initialize each GPIO object with output mode and no internal pull-up/down resistor, and append them to the IOlist
IOlist.append(Pin(Pin.GPIO34, Pin.OUT, Pin.PULL_DISABLE, 0))
IOlist.append(Pin(Pin.GPIO32, Pin.OUT, Pin.PULL_DISABLE, 0))
IOlist.append(Pin(Pin.GPIO31, Pin.OUT, Pin.PULL_DISABLE, 0))
IOlist.append(Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0))
IOlist.append(Pin(Pin.GPIO2, Pin.OUT, Pin.PULL_DISABLE, 0))
IOlist.append(Pin(Pin.GPIO3, Pin.OUT, Pin.PULL_DISABLE, 0))

while True:
    for y in IOlist:            # Loop through each GPIO object in the IOlist
        for x in IOlist:        # Turn off all GPIO objects before lighting up the next one
            x.write(1)  
        y.write(0)              # Light up the current GPIO object
        utime.sleep_ms(500)     # Wait for 500ms before lighting up the next GPIO object


from machine import Pin
import utime

IOlist = []  # Create an empty list
# Initialize GPIO and add IOlist
IOlist.append(Pin(Pin.GPIO34, Pin.OUT, Pin.PULL_DISABLE, 0))  
IOlist.append(Pin(Pin.GPIO32, Pin.OUT, Pin.PULL_DISABLE, 0))  
IOlist.append(Pin(Pin.GPIO31, Pin.OUT, Pin.PULL_DISABLE, 0))  
IOlist.append(Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0))  
IOlist.append(Pin(Pin.GPIO2, Pin.OUT, Pin.PULL_DISABLE, 0))  
IOlist.append(Pin(Pin.GPIO3, Pin.OUT, Pin.PULL_DISABLE, 0))  


while True:
    for y in IOlist:            # LED lighting one by one
        for x in IOlist:        # All LED off
            x.write(1)  
        y.write(0)              # Light up the LED
        utime.sleep_ms(500)     # Turn on the next LED after a delay
