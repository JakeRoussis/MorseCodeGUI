from tkinter import *
import tkinter.font
import time
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Pinouts
led = LED(14)

## Definitions
win = Tk()
win.title('LED Toggle')
myFont = tkinter.font.Font(family='Helvetica', size=12, weight='bold')
eField_text = StringVar()

## GUI Commands
def blink():
    eStr = eField_text.get()
    i = 0
    while i < len(eStr):
        checkChar(eStr[i].lower())
        i += 1
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()

## Widgets
Label(win, text='Word to morse code: ').grid(row=0)
eField = Entry(win, textvariable=eField_text)
eField.grid(row=0, column=1)

blinkButton = Button(win, text='BLINK', font=myFont, command=blink, bg='grey', height=1, width=12,)
blinkButton.grid(row=1, column=0)
exitButton = Button(win, text='EXIT', font=myFont, command=close, bg='red', height=1, width=12,)
exitButton.grid(row=1, column=1)

def character_limit(eField_text):
    if len(eField_text.get()) > 0:
        eField_text.set(eField_text.get()[:12])

eField_text.trace('w', lambda *args: character_limit(eField_text))

def dot(num):
    for i in range(0, num):
        led.on()
        time.sleep(0.4)
        led.off()
        time.sleep(0.4)

def dash(num):
    for i in range(0, num):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

def shortspace():
    time.sleep(0.5)
def lA():
    dot(1)
    dash(1)
    shortspace()
def lB():
    dash(1)
    dot(3)
    shortspace()
def lC():
    dot(1)
    dash(1)
    dot(1)
    shortspace()
def lD():
    dot(2)
    shortspace()
def lE():
    dot(1)
    shortspace()
def lF():
    dot(2)
    dash(1)
    dot(1)
    shortspace()
def lG():
    dash(2)
    dot(1)
    shortspace()
def lH():
    dot(4)
    shortspace()
def lI():
    dot(2)
    shortspace()
def lJ():
    dot(1)
    dash(3)
    shortspace()
def lK():
    dash(1)
    dot(1)
    dash(1)
    shortspace()
def lL():
    dot(1)
    dash(1)
    dot(2)
    shortspace()
def lM():
    dash(2)
    shortspace()
def lN():
    dash(1)
    dot(1)
    shortspace()
def lO():
    dash(3)
    shortspace()
def lP():
    dot(1)
    dash(2)
    dot(1)
    shortspace()
def lQ():
    dash(2)
    dot(1)
    dash(1)
    shortspace()
def lR():
    dot(1)
    dash(1)
    dot(1)
    shortspace()
def lS():
    dot(3)
    shortspace()
def lT():
    dash(1)
    shortspace()
def lU():
    dot(2)
    dash(1)
    shortspace()
def lV():
    dot(3)
    dash(1)
    shortspace()
def lW():
    dot(1)
    dash(1)
    shortspace()
def lX():
    dash(1)
    dot(2)
    dash(1)
    shortspace()
def lY():
    dash(1)
    dot(1)
    dash(2)
    shortspace()
def lZ():
    dash(2)
    dot(2)
    shortspace()
def n1():
    dot(1)
    dash(3)
    shortspace()
def n2():
    dot(2)
    dash(3)
    shortspace()
def n3():
    dot(3)
    dash(2)
    shortspace()
def n4():
    dot(4)
    dash(1)
    shortspace()
def n5():
    dot(5)
    shortspace()
def n6():
    dash(1)
    dot(4)
    shortspace()
def n7():
    dash(2)
    dot(3)
    shortspace()
def n8():
    dash(3)
    dot(2)
    shortspace()
def n9():
    dash(4)
    dot(1)
    shortspace()
def n0():
    dash(5)
    shortspace()
def space():
    time.sleep(0.8)

def checkChar(char):
    if char == 'a': lA()
    if char == 'b': lB()
    if char == 'c': lC()
    if char == 'd': lD()
    if char == 'e': lE()
    if char == 'f': lF()
    if char == 'g': lG()
    if char == 'h': lH()
    if char == 'i': lI()
    if char == 'j': lJ()
    if char == 'k': lK()
    if char == 'l': lL()
    if char == 'm': lM()
    if char == 'n': lN()
    if char == 'o': lO()
    if char == 'p': lP()
    if char == 'q': lQ()
    if char == 'r': lR()
    if char == 's': lS()
    if char == 't': lT()
    if char == 'u': lU()
    if char == 'v': lV()
    if char == 'w': lW()
    if char == 'x': lX()
    if char == 'y': lY()
    if char == 'z': lZ()
    if char == '': space()
    if char == '0': n0()
    if char == '1': n1()
    if char == '2': n2()
    if char == '3': n3()
    if char == '4': n4()
    if char == '5': n5()
    if char == '6': n6()
    if char == '7': n7()
    if char == '8': n8()
    if char == '9': n9()


win.protocol('WM_DELETE_WINDOW', close)
win.mainloop()
