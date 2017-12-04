import RPi.GPIO as gpio
import time
import sys
 
# get one key from terminal 
def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch
 
def Enable(num):
    gpio.output(num, True)
 
def Disable(num):
    gpio.output(num, False)
 
def Forward():
    Enable(13)
    Disable(15)
 
    Enable(18)
    Disable(22)
 
def Backward():
    Disable(13)
    Enable(15)
 
    Disable(18)
    Enable(22)
 
def TurnLeft():
    Disable(13)
    Disable(15)
 
    Enable(18)
    Disable(22)
 
def TurnRight():
    Enable(13)
    Disable(15)
 
    Disable(18)
    Disable(22)
 
def StopCar():
    Disable(13)
    Disable(15)
    Disable(18)
    Disable(22)
 
def SetAsOut(num):
    gpio.setup(num, gpio.OUT)
 
def Setup():
    gpio.setmode(gpio.BOARD)
    SetAsOut(13)
    SetAsOut(15)
    # SetAsOut(7)
    # SetAsOut(11)
 
    SetAsOut(12)
    SetAsOut(16)
    SetAsOut(18)
    SetAsOut(22)
 
    # Enable(7)
    # Enable(11)
 
    Enable(12)
    Enable(16)
 
 
Setup()
chfunc = getch()
 
try:
    while True:
        c = chfunc()
        print(c)
        if c=='1':
            print('forward')
            Forward()
        elif c=='2':
            print('backward')
            Backward()
        elif c=='3':
            print('turn left')
            TurnLeft()
        elif c=='4':
            print('turn right')
            TurnRight()
        elif c=='5' or c=='6' or c=='7' or c=='8':
            print('stop car')
            StopCar()
        elif c=='9' or c=='0':
            print('exit')
            gpio.cleanup()
            break
        else:
            print('no such command')
 
except KeyboardInterrupt:
    print('keyboard interrupted...!')
    gpio.cleanup()

