# IMPORTS
from gpiozero import DigitalOutputDevice
from gpiozero import Button
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
import time

IP_ADDRESS = PiGPIOFactory('192.168.0.207')
# VARIABLES
SECOND_PUSH = 1.5
THIRD_PUSH = 2.0

# SETUP RELAY
RELAY1 = 1
RELAY2 = 2
RELAY3 = 3
RELAY4 = 4
CHANNEL = [RELAY1, RELAY2, RELAY3, RELAY4]

# SETUP LED'S
LED1 = LED()
LED2 = (2, True)
LED3 = (3, True)
LED4 = (4, True)
LED = [LED1, LED2, LED3, LED4]

# SETUP BUTTONS
BUTTON1 = Button(1)
BUTTON2 = 2
BUTTON3 = 3
BUTTON4 = 4
BTN_PIN = [BUTTON1, BUTTON2, BUTTON3, BUTTON4]

# LISTS
relay = [RELAY1, RELAY2, RELAY3, RELAY4]
buttons = [BUTTON1, BUTTON2, BUTTON3, BUTTON4]
leds = [LED1, LED2, LED3, LED4]

# FUNCTIONS
print(BUTTON1)

def button1_press():
    if BUTTON1.value:
        RELAY1.on()
        LED1.on()
        time.sleep(0.50)
    if BUTTON1.value:
        RELAY1.off()
        LED1.off()
        time.sleep(0.50)

def button_pressed():
    if BUTTON1.value:
        LED1.on()
        time.sleep(0.50)
    if BUTTON1.value:
        LED1.off()
        time.sleep(0.50)









