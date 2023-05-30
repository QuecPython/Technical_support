"""
Please refer to the Chinese information:https://python.quectel.com/doc/API_reference/zh/
Please refer to English information:    https://python.quectel.com/doc/doc/API_reference/en/
"""
"""
This code snippet creates a Python script that utilizes the machine module to control GPIO pins on a device. In this particular example, the code sets up a single GPIO pin with pin number 26 as output and without pull-up or pull-down resistor enabled.

The code then enters an infinite loop where it repeatedly toggles the GPIO pin state between high and low with a 2 second delay between each state change.

Each time the state of a GPIO pin changes, the current pin status (either HIGH or LOW) is printed to the console along with the pin number. This allows the user to monitor the state of each GPIO pin and verify that the code is working correctly.

Overall, the code demonstrates how to use the machine module to control GPIO pins in a Python script, making it useful for a variety of hardware projects and applications.
"""

# Importing necessary libraries
from machine import Pin     # Importing Pin module from machine library for GPIO control
import utime                # Importing utime module for time control

# Creating an empty list to store the IO pins
IOlist = []

# Adding Pin objects to the list
IOlist.append(Pin(Pin.GPIO26, Pin.OUT, Pin.PULL_DISABLE, 0))

# Infinite loop for controlling the IO pins
while True:
    # Looping through each IO pin and setting its state to HIGH (1)
    for x in range(int(len(IOlist))):
        print(IOlist[x], 'GPIO{}'.format(x + 1))    # Printing the current IO pin status
        IOlist[x].write(1)                          # Setting the current IO pin state to HIGH
    utime.sleep_ms(2000)                            # Waiting for 2 seconds

    # Looping through each IO pin and setting its state to LOW (0)
    for x in range(int(len(IOlist))):
        print(IOlist[x], 'GPIO{}'.format(x + 1))    # Printing the current IO pin status
        IOlist[x].write(0)                          # Setting the current IO pin state to LOW
    utime.sleep_ms(2000)                            # Waiting for 2 seconds
