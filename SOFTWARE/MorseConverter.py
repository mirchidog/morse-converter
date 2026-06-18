'''
MorseConverter.py
for Morse Converter, a PCB that outputs Morse Code from text

by R3C_
'''

import machine
from machine import Pin
import utime
from typing import Undefined, List

# Configure keypad as inputs
buttonABC = Pin(14, Pin.IN, Pin.PULL_UP)
buttonDEF = Pin(13, Pin.IN, Pin.PULL_UP)
buttonGHI = Pin(12, Pin.IN, Pin.PULL_UP)
buttonJKL = Pin(10, Pin.IN, Pin.PULL_UP)
buttonMNO = Pin(9, Pin.IN, Pin.PULL_UP)
buttonPQR = Pin(11, Pin.IN, Pin.PULL_UP)
buttonSTUV = Pin(6, Pin.IN, Pin.PULL_UP)
buttonWXYZ = Pin(7, Pin.IN, Pin.PULL_UP)
buttonENTER = Pin(8, Pin.IN, Pin.PULL_UP)

# Create message string
message = Undefined(list(str))
messageOver = False

# Initialize the buzzer
buzzer = machine.PWM(machine.Pin(25))
buzzer.freq(550)
buzzer.duty(0)



# Store the typed letters
def readLetter():
    while buttonENTER.value() == 1:
        if buttonABC.value() == 0:
            keyClicked = 1
            keyCount += 1
        elif buttonDEF.value() == 0:
            keyClicked = 2
            keyCount += 1
        elif buttonGHI.value() == 0:
            keyClicked = 3
            keyCount += 1
        elif buttonJKL.value() == 0:
            keyClicked = 4
            keyCount += 1
        elif buttonMNO.value() == 0:
            keyClicked = 5
            keyCount += 1
        elif buttonPQR.value() == 0:
            keyClicked = 6
            keyCount += 1
        elif buttonSTUV.value() == 0:
            keyClicked = 7
            keyCount += 1
        elif buttonWXYZ.value() == 0:
            keyClicked = 8
            keyCount += 1



# Output Morse code according to stored letter
def outputMorse():
    # (When ENTER key is pressed,...)
    if buttonENTER.value() == 0:
        wordGap()
        if buttonENTER.value() == 0:
            messageOver = True
    elif keyClicked == 1:
        if keyCount == 1:   #A
            dot()
            dash()
        elif keyCount == 2: #B
            dot()
            dot()
            dot()
        else:               #C
            dash()
            dot()
            dash()
            dot()
    elif keyClicked == 2:
        if keyCount == 1:   #D
            dash()
            dot()
            dot()
        elif keyCount == 2: #E
            dot()
        else:               #F
            dot()
            dot()
            dash()
            dot()
    elif keyClicked == 3:
        if keyCount == 1:   #G
            dash()
            dash()
            dot()
        elif keyCount == 2: #H
            dot()
            dot()
            dot()
            dot()
        else:               #I
            dot()
            dot()
    elif keyClicked == 4:
        if keyCount == 1:   #J
            dot()
            dash()
            dash()
            dash()
        elif keyCount == 2: #K
            dash()
            dot()
            dash()
        else:               #L
            dot()
            dash()
            dot()
            dot()
    elif keyClicked == 5:
        if keyCount == 1:   #M
            dash()
            dash()
        elif keyCount == 2: #N
            dash()
            dot()
        else:               #O
            dash()
            dash()
            dash()
    elif keyClicked == 6:
        if keyCount == 1:   #P
            dot()
            dash()
            dash()
            dot()
        elif keyCount == 2: #Q
            dash()
            dash()
            dot()
            dash()
        else:               #R
            dot()
            dash()
            dot()
    elif keyClicked == 7:
        if keyCount == 1:   #S
            dot()
            dot()
            dot()
        elif keyCount == 2: #T
            dash()
        elif keyCount == 3: #U
            dot()
            dot()
            dash()
        else:               #V
            dot()
            dot()
            dot()
            dash()
    elif keyClicked == 8:
        if keyCount == 1:   #W
            dot()
            dash()
            dash()
        elif keyCount == 2: #X
            dash()
            dot()
            dot()
            dash()
        elif keyCount == 3: #Y
            dash()
            dot()
            dash()
            dash()
        else:               #Z
            dash()
            dash()
            dot()
            dot()
    space()



# Define length of dot dash and spaces
def dot():
    buzzer.duty(512)
    utime.sleep_ms(200)

def dash():
    buzzer.duty(512)
    utime.sleep_ms(600)

def space():
    buzzer.duty(0)
    utime.sleep_ms(600)

def wordGap():
    buzzer.duty(0)
    utime.sleep_ms(800) # 1400ms - SPACE



# Run program
while messageOver == False:
    keyCount = 0
    # Times a key is pressed in a sequence
    keyClicked = 0
    # Which key is pressed

    readLetter()
    outputMorse()
