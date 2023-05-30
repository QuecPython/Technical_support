"""
Please refer to the Chinese information:https://python.quectel.com/doc/API_reference/zh/
Please refer to English information:    https://python.quectel.com/doc/doc/API_reference/en/
"""

"""
This code is designed to detect when a key button connected to GPIO 12 on a microcontroller has been pressed or released. Its functionality is broken down into separate functions:

timer0_callback(t0) - Executes every 100ms and increments t0Count if it's less than 20.
key_callback(status) - Recognizes if the button has been pressed or released, starts/stops the timer, and prints Long press key or Short press key depending on the length of the press.
thread_KEY() - Monitors the state of the key button continuously using a while loop and calls key_callback(status) accordingly.
The variables and objects used in the functions are defined globally to maintain continuity and accessibility throughout the entire script. Additionally, comments have been added to provide explanations for each function and make the code easier to understand.
"""

from machine import Pin, Timer
import utime
import _thread

# Set up the GPIO object as a global variable for global availability
key = Pin(Pin.GPIO12, Pin.IN, Pin.PULL_PD , 1)

t0Count = 0

def timer0_callback(t0):
    # Increment the timer count each time this function is executed
    global t0Count
    t0Count = t0Count>=20 and t0Count or t0Count + 1
    print('t0Count=', t0Count)

# Allocate the Timer object as a global variable to allow for global access
t0 = Timer(Timer.Timer0)

def key_callback(status):
    global t0Count
    if status == 0: # Key button has been released
        print('powerkey release.')
        t0.stop() # Stop the timer object
        print('t0Count=', t0Count)
        if t0Count >= 20:
            print('Long press key')  
        else:
            print('Short press key')  

        t0Count = 0 # Reset the timer count to zero
    elif status == 1: # Key button has been pressed
        t0.start(period=100, mode=t0.PERIODIC, callback=timer0_callback)  
        # Start the timer object with a periodic period of 100ms and set its callback function
        print('t0Count=', t0Count)

def thread_KEY():
    while True:
        utime.sleep_ms(20)
        if key.read() == 1: # If the key is not pressed, continue
            continue
        while key.read() == 0: # If the key is pressed down
            key_callback(1) # Call the key callback function with value 1 (pressed down)
            utime.sleep_ms(20)
        key_callback(0) # Call the key callback function with value 0 (released)

_thread.start_new_thread(thread_KEY, ())  # Start a new thread for monitoring the key button





