#!/usr/bin/env

__author__ = "Zino Henderickx"
__version__ = "3.2"

# LIBRARIES
from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import multiprocessing
import time
import timeit

IP = PiGPIOFactory('192.168.0.207')
BOUNCE_TIME = 0.01
PUSH_TIME = 1
PUSH_TIME2 = 2
PUSH_TIME3 = 3
PUSH_TIME4 = 4


# LED's
AMOUNT_LEDS = 4
LED1 = LED(17, pin_factory=IP)
LED2 = LED(27, pin_factory=IP)
LED3 = LED(22, pin_factory=IP)
LED4 = LED(10, pin_factory=IP)


# BUTTONS
AMOUNT_BUTTONS = 4
BUTTON1 = Button(26, pin_factory=IP)
BUTTON2 = Button(6, pin_factory=IP)
BUTTON3 = Button(13, pin_factory=IP)
BUTTON4 = Button(19, pin_factory=IP)


# LISTS

led = []
button = []


def button_push():
    if BUTTON1.value == 1:
        start = time.time()
        times_pushed = 1
        end = time.time()
        time_elapsed = end - start
        print(time_elapsed)
        if BUTTON1.value == 1 and time_elapsed < PUSH_TIME:
            times_pushed = 1
            LED1.on()
        if BUTTON1.value == 1 and time_elapsed > PUSH_TIME:
            times_pushed = 2
            LED1.blink(1, 1, None, True)
            print(times_pushed)
            check_button_1()
        if BUTTON1.value == 1 and time_elapsed > PUSH_TIME:
            times_pushed = 3
            LED3.off()
            print(times_pushed)
            check_button_1()


def check_button_1():
    if BUTTON1.value == 1 and LED1.value == 0:
        LED1.on()
        time.sleep(0.50)
    if BUTTON1.value == 1 and LED1.value == 1:
        LED1.off()
        time.sleep(0.50)


# MAIN START PROGRAM


if __name__ == "__main__":
    x1 = multiprocessing.Process(target=button_push)
    x2 = multiprocessing.Process(target=check_button_1)
    x1.start()
    x2.start()