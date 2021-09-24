#!/usr/bin/env python3

from autopilot.input import Mouse
import threading

mouse = Mouse.create()

interval = 20

def moveMouse():
    mouse.move(100, 50)
    mouse.move(300, 50)
    # mouse.click()
    # print("This loops on a timer every %d seconds" % interval)

def startTimer():
    threading.Timer(interval, startTimer).start()
    moveMouse()

startTimer()