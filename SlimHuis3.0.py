#!/usr/bin/env

__author__ = "Zino Henderickx"
__version__ = "1.1"

# LIBRARIES
from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time

IP = PiGPIOFactory('192.168.0.207')
max_time = 1
max_time_2 = 2
max_time_3 = 3
max_time_4 = 4
pressed = time.time()


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


def button_1():
    if BUTTON1.value == 1:
        LED1.on()
        time.sleep(0.50)
    if BUTTON1.value == 0:
        LED1.off()
        time.sleep(0.50)


def button_2():
    if BUTTON2.value == 1:
        LED2.on()
        time.sleep(0.50)
    if BUTTON2.value == 0:
        LED2.off()
        time.sleep(0.50)


def button_3():
    if BUTTON3.value == 1:
        LED3.on()
        time.sleep(0.50)
    if BUTTON3.value == 0:
        LED3.off()
        time.sleep(0.50)


def button_4():
    if BUTTON4.value == 1:
        LED4.on()
        time.sleep(0.50)
    if BUTTON4.value == 0:
        LED4.off()
        time.sleep(0.50)


while button_1():
    time.sleep(1.0)
    if button_1() == pressed:
        when_pressed = time.time()
        while time.time() - when_pressed < max_time:
            time.sleep(1.0)
            if button_1 == pressed:
                LED1.on()

while button_2():
    time.sleep(2.0)
    if button_2() == pressed:
        when_pressed = time.time()
        while time.time() - when_pressed < max_time:
            time.sleep(1.0)
            if button_2 == pressed:
                LED2.on()

while button_3():
    time.sleep(3.0)
    if button_3() == pressed:
        when_pressed = time.time()
        while time.time() - when_pressed < max_time:
            time.sleep(1.0)
            if button_3 == pressed:
                LED3.on()

while button_4():
    time.sleep(4.0)
    if button_4() == pressed:
        when_pressed = time.time()
        while time.time() - when_pressed < max_time:
            time.sleep(1.0)
            if button_4 == pressed:
                LED4.on()


def main():
    button_1()
    button_2()
    button_3()
    button_4()

# MAIN START PROGRAM


if __name__ == "__main__":
    main()



