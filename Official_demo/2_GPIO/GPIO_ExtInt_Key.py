"""
Please refer to the Chinese information:https://python.quectel.com/doc/API_reference/zh/
Please refer to English information:    https://python.quectel.com/doc/doc/API_reference/en/
"""
"""
This code snippet creates a Python script that utilizes the machine module to set up and handle external 
interrupts on two GPIO pins. In this particular example, the first interrupt is triggered by a rising edge 
on pin GPIO12 with a pull-down resistor enabled, and the second interrupt is triggered by a falling 
edge on pin GPIO13 with a pull-up resistor enabled.

The code defines two callback functions, callback1() and callback2(), that are executed each time an external 
interrupt is triggered. Within each callback function, a global variable is incremented to keep track of the 
number of times the interrupt has occurred, and the current count and state of the interrupt are printed to the console.

The code also defines a main() function that initializes the global variables, creates the external interrupt objects, 
enables the interrupts, and enters an infinite loop. Within this loop, the code pauses for 5 seconds before printing 
a message to indicate that the main loop is still running.

Overall, the code demonstrates how to use the machine module to handle external interrupts in a Python script, 
making it useful for a variety of sensor input and event-driven applications.
"""

# Importing necessary libraries
from machine import ExtInt  # Importing ExtInt module from machine library for external interrupts
import utime  # Importing utime module for time control

# Defining callback functions for the two external interrupts
def callback1(args):
    global A  # Global variable used to count the number of times the first interrupt occurs
    A +=1
    print('Count A:{},state:{}'.format(A, args))  # Printing the current count and state of the first interrupt
    print("callback1")

def callback2(args):
    global B  # Global variable used to count the number of times the second interrupt occurs
    B += 1
    print('Count B:{},state:{}'.format(B, args))  # Printing the current count and state of the second interrupt
    print("callback2")

def main():
    global A  # Global variable used by both callback functions
    global B  # Global variable used by both callback functions
    global extint1  # The external interrupt object for the first interrupt
    global extint2  # The external interrupt object for the second interrupt

    A = 0  # Initializing the first interrupt count
    B = 0  # Initializing the second interrupt count

    # Creating the first external interrupt object on pin GPIO12 with rising edge trigger and pull-down resistor enabled
    extint1 = ExtInt(ExtInt.GPIO12, ExtInt.IRQ_RISING, ExtInt.PULL_PD, callback1)
    extint1.enable()  # Enabling the first interrupt

    # Creating the second external interrupt object on pin GPIO13 with falling edge trigger and pull-up resistor enabled
    extint2 = ExtInt(ExtInt.GPIO13, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, callback2)
    extint2.enable()  # Enabling the second interrupt
    
    while True:
        utime.sleep_ms(5000)  # Delaying for 5 seconds before continuing
        print("main loop running")  # Printing a message to indicate that the main loop is still running

if __name__ == '__main__':
    main()




