import threading
import sys

interval = 1
counter = 0

def myPeriodicFunction():
    global counter
    counter += 1
    sys.stdout.write("\r%d" % counter)
    sys.stdout.flush()

def startTimer():
    threading.Timer(interval, startTimer).start()
    myPeriodicFunction()

startTimer()
