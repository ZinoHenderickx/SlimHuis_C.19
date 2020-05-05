#!/usr/bin/env

__author__ = "Zino Henderickx"
__version__ = "1.0"

# LIBRARIES
from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time

IP = PiGPIOFactory('192.168.0.207')

# LED's
LED1 = LED(17, pin_factory=IP)
LED2 = LED(27, pin_factory=IP)
LED3 = LED(22, pin_factory=IP)
LED4 = LED(10, pin_factory=IP)


# BUTTONS
BUTTON1 = Button(5, pin_factory=IP)
BUTTON2 = Button(6, pin_factory=IP)
BUTTON3 = Button(13, pin_factory=IP)
BUTTON4 = Button(19, pin_factory=IP)

# LISTS
led = [10, 17, 22, 27]
button = [5, 6, 13, 19]

# FUNCTIONS


def set_up_led():
    for i in range(LED1):
        led.append(LED[i])
        print(led)


def set_up_button():
    for i in range(BUTTON1):
        button.append(Button(pin=button[i], pull_up=False, bounce_time=0.25))
        print(button)


def toggle_button(button_nr):
    if button[button_nr].value == 1 and led[button_nr].value == 0:
        led[button_nr].on()
        time.sleep(0.25)

    if button[button_nr].value == 1 and led[button_nr].value == 1:
        led[button_nr].off()
        time.sleep(0.25)


def check_button():
    while True:
        for i in range(BUTTON1):
            toggle_button(i)


def main():
    set_up_led()
    set_up_button()
    check_button()

# MAIN START PROGRAM


if __name__ == "__main__":
    main()





