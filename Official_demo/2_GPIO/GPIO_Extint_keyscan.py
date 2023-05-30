"""
Please refer to the Chinese information:https://python.quectel.com/doc/API_reference/zh/
Please refer to English information:    https://python.quectel.com/doc/doc/API_reference/en/
"""
    
# Import necessary modules
from machine import ExtInt, Pin
from utime import sleep_ms
from queue import Queue
import _thread

# Create a queue object to hold any events related to pressed keys
key_evt_queue = Queue(8)

# Function to handle and dispatch key events in a separate thread
def key_evt_thread_entry():
    while True:
        # Wait for an event to be added to the queue
        sleep_ms(1)
        if not key_evt_queue.empty():
            # Retrieve the callback function, pin number, and event type from the queue
            event_cb, pin, event = key_evt_queue.get() 
            # Call the specified callback function with the retrieved parameters
            event_cb(pin, event)

# Start a new execution thread running the key event dispatcher function
_thread.start_new_thread(key_evt_thread_entry, ()) 

# Define a class to abstract the concept of a physical key button
class Key():

    # Define constants representing the two types of key events (pressed or released)
    class Event():
        PRESSED = 0x01
        RELEASED = 0x02

    # Define a custom exception class to be raised if unexpected values are passed as object parameters
    class Error(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)
        
    # Constructor method for creating a new Key instance.
    # Parameters:
    # - pin: The GPIO pin number to which the key is connected
    # - level_on_pressed: Sets whether the associated GPIO input pin has a pull-up or pull-down resistor (0 for pull-up, 1 for pull-down)
    # - cared_event: A bitfield describing the desired event(s) to be detected by the key object (preferably using the Key.Event constants set earlier) 
    # - event_cb: A callback function to be executed when a key event is detected
    def __init__(self, pin, level_on_pressed, cared_event, event_cb):
        # Validate and store the provided parameters
        self.pin = pin
        if level_on_pressed == 0: 
            self.exti_pull = ExtInt.PULL_PU 
            if cared_event == self.Event.PRESSED:
                self.exti_trigger_mode = ExtInt.IRQ_FALLING 
            elif cared_event == self.Event.RELEASED:
                self.exti_trigger_mode = ExtInt.IRQ_RISING 
            elif cared_event == self.Event.PRESSED | self.Event.RELEASED: 
                self.exti_trigger_mode = ExtInt.IRQ_RISING_FALLING 
            else:
                raise self.Error("Value error of <cared_event>!")
        elif level_on_pressed == 1: 
            self.exti_pull = ExtInt.PULL_PD 
            if cared_event == self.Event.PRESSED:
                self.exti_trigger_mode = ExtInt.IRQ_RISING 
            elif cared_event == self.Event.RELEASED:
                self.exti_trigger_mode = ExtInt.IRQ_FALLING
            elif cared_event == self.Event.PRESSED | self.Event.RELEASED:
                self.exti_trigger_mode = ExtInt.IRQ_RISING_FALLING
            else:
                raise self.Error("Value error of <cared_event>!")
        else:
            raise self.Error("Value error of <level_on_pressed>!")

        self.level_on_pressed = level_on_pressed
        self.cared_event = cared_event
        self.event_cb = event_cb
        # Create an external interrupt object on the specified pin using the configured settings and passing the exit_cb method as the ISR
        self.exti = ExtInt(self.pin, self.exti_trigger_mode, self.exti_pull, self.exit_cb) 
        # Enable the interrupt object
        self.exti.enable()
    
    # This method is called when a key is triggered by an interrupt.
    # It first disables the current ExtInt object and reads the level voltage of the GPIO pin associated with the key. 
    # Depending on the GPIO voltage level, it determines whether the corresponding event (pressed/released) has occurred. 
    # The event is then pushed to the shared key event queue in the format of (callback_function, pin_number, event_type).
    # The method finishes by re-enabling the ExtInt object for the key.

    def exit_cb(self, args):
        self.exti.disable()  # Disable the current ExtInt object.
        sleep_ms(20)  # Wait briefly to allow any voltage abnormalities to settle.
        
        gpio = Pin(args[0], Pin.IN, Pin.PULL_PU, 1)  # Create a Pin object for the associated GPIO pin.
        level = gpio.read()  # Read the current GPIO level.

        event = None
        # Determine if the corresponding event (pressed/released) has occurred based on the GPIO voltage level.
        if self.level_on_pressed == 0:  
            if self.cared_event == self.Event.PRESSED and level == 0:
                event = self.cared_event                             
            if self.cared_event == self.Event.RELEASED and level == 1:
                event = self.cared_event
            if self.cared_event == self.Event.PRESSED | self.Event.RELEASED:
                if level == 0: 
                    event = self.Event.PRESSED
                else:
                    event = self.Event.RELEASED
        else: 
            if self.cared_event == self.Event.PRESSED and level == 1:
                event = self.cared_event
            if self.cared_event == self.Event.RELEASED and level == 0:
                event = self.cared_event
            if self.cared_event == self.Event.PRESSED | self.Event.RELEASED:
                if level == 1:
                    event = self.Event.PRESSED
                else:
                    event = self.Event.RELEASED
        
        # Add the event to the shared key event queue in the format of (callback function, pin number, event type).
        if event:
            key_evt_queue.put((self.event_cb, self.pin, event))
        
        # Re-enable the ExtInt object for the key.
        self.exti = ExtInt(self.pin, self.exti_trigger_mode, self.exti_pull, self.exit_cb)
        self.exti.enable()

# Main entry point of the program. It sets up two GPIO pins as keys (k1 and k2) and registers their events.
# When an event occurs, the event_cb() function is called with arguments specifying the pin and event type.
# The event_cb() function then handles the corresponding key press or release event.
if __name__ == '__main__':
    # Set up the GPIO pins for the two keys
    k1 = Pin.GPIO4 
    k2 = Pin.GPIO30 

    def event_cb(pin, event): 
        # Handle the key press/release event based on the pin number and event type.
        if pin == k1:
            if event == Key.Event.PRESSED: 
                print("k1 pressed")
            else:
                print("k1 released")
        if pin == k2:
            if event == Key.Event.PRESSED: 
                print("k2 pressed")
            else:
                print("k2 released")

    # Register the events for both keys and pass the event callback function.
    Key(k1, 0, Key.Event.PRESSED | Key.Event.RELEASED, event_cb) 
    Key(k2, 0, Key.Event.PRESSED | Key.Event.RELEASED, event_cb)
